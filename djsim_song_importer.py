import os,sys,shutil,json
import numpy as np
import librosa
import librosa.filters
from scipy.signal import butter, sosfilt

from PIL import Image

import PySide2
from PySide2 import QtWidgets
from PySide2.QtWidgets import QMainWindow, QApplication, QFileDialog, QMessageBox
from PySide2.QtGui import QPixmap
from PySide2.QtCore import QByteArray, QBuffer, Qt
#from pyqtgraph import PlotWidget
import pyqtgraph as pg

import resources_rc
from ui_djsim_song_importer import Ui_MainWindow

import matplotlib
matplotlib.use('Agg')

import matplotlib.pyplot as plt
plt.ioff()
from matplotlib.colors import to_rgb



#import soundfile as sf
from pydub import AudioSegment
# Set the ffmpeg path
AudioSegment.converter = r"./bin/ffmpeg.exe"

import music_tag


app = QApplication(sys.argv)


class MainWindow(QMainWindow, Ui_MainWindow):
    is_loaded_file = False
    album_art = None
    file_path = None
    folder_path = None
    ready = False
    raw_data = None
    sr = None
    id3tag = None
    DECIMATION_FACTOR = 10
    DEFAULT_PREVIEW_LENGTH = 90
    PREVIEW_LENGTH = 90
    BEAT_OFFSET = 0.0
    last_beat_time = 2.0
    songStartItem = pg.InfiniteLine(pos=0.0, angle=90, pen=pg.mkPen((191,0,201), width=3))
    songStartItem.setZValue(50)

    skipBeatsItem = pg.InfiniteLine(pos=0.0, angle=90, pen=pg.mkPen('g', width=3))
    skipBeatsItem.setZValue(49)
    
    song_start_time = 0.0
    plot_item = None

    skip_beats = 0

    raw_song_length = 0.0
    
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        self.setupUi(self)
        self.init_ui()

    def init_ui(self):
        self.plot_item = self.graphWidget.getPlotItem()
        self.loadFileBtn.clicked.connect(self.get_file)
        self.loadImageBtn.clicked.connect(self.get_album_art)
        self.convertBtn.clicked.connect(self.convert_file)
        self.filenameLabel.setText("")

        self.beatMarkers = []

        self.BPMBox.valueChanged.connect(self.update_beat_grid)
        self.skipBeatsBox.valueChanged.connect(self.update_beat_grid)
        
        self.offsetResetBtn.clicked.connect(self.reset_beat_grid)
        self.analyseBPMBtn.clicked.connect(self.estimate_BPM)

        self.style_graph()

    def style_graph(self):
        self.plot_item.setMouseEnabled(y=False)
        self.plot_item.setMenuEnabled(False)

        # Configure the plot to look nicer
        self.graphWidget.setBackground((15,22,26))
        #(15,22,26)   darker
        #(28,37,44)   dark
        #(255,86,108) red
        #(0,182,117)  green
        #(191,0,201) purple

        # Disable the vertical axis
        self.plot_item.showAxis('left', show=False)
        self.plot_item.showAxis('bottom', show=True)
        self.graphWidget.scene().sigMouseClicked.connect(self.handle_click)
        # Configure the horizontal axis (time in seconds)
        bottom_axis = self.plot_item.getAxis('bottom')  # Get the bottom axis
        #axis.setLabel('Time (s)')  # Label the x-axis
        bottom_axis.hide()
        
        self.graphWidget.setYRange(-1, 1, padding=0)  # Assuming normalized audio data

    def update_status(self, message):
        self.statusBar.showMessage(message)  # Show the new message for 10 seconds
        QApplication.processEvents()



    def update_graph(self, audio_data, sr):
        # Clear previous data
        self.graphWidget.clear()
        #self.graphWidget.getPlotItem().setTitle("ALIGN BEATGRID (MAX {} SECOND PREVIEW - CHECK BPM)".format(self.PREVIEW_LENGTH))
        
        #warning_text = pg.TextItem("(not full song)", anchor=(-1,-0.5))
        #self.graphWidget.addItem(warning_text)
        
        if audio_data is not None and len(audio_data) > 0:
            # Create the time array for x-axis
            t = np.arange(len(audio_data)) / sr

            # Plot the data
            self.graphWidget.plot(t[::10], audio_data[::10],pen=pg.mkPen(0,182,117))

            # Configure the horizontal axis (time in seconds) with ticks every second
            max_time = len(audio_data) / sr
            ticks = [(i, f'{i:.0f}') for i in range(int(max_time) + 1)]  # Generate ticks for each second
            axis = self.graphWidget.getPlotItem().getAxis('bottom')
            axis.setTicks([ticks])

            
            self.graphWidget.addItem(self.songStartItem)
            self.graphWidget.addItem(self.skipBeatsItem)
            

        else:
            # No audio data to plot, consider displaying a message or leaving the graph blank
            print("No audio data available to plot.")

        # Set reasonable x and y ranges even if data is zero or not loaded
        self.graphWidget.setXRange(0.0,2.0)#0, max_time if audio_data is not None and len(audio_data) > 0 else 1, padding=0)
        self.graphWidget.setYRange(-1, 1, padding=0)  # Assuming normalized audio data

    def reset_beat_grid(self,new_load=False):
        self.BEAT_OFFSET = 0.0
        self.update_start_time(0.0)
        self.timeOffsetLabel.setText(str(self.BEAT_OFFSET))
        if not new_load:
            self.update_beat_grid()
        
    def update_beat_grid(self):
        bpm = self.BPMBox.value()
        seconds_per_beat = 60 / bpm

        # Clear existing beat markers
        for line in self.beatMarkers:
            self.graphWidget.removeItem(line)
        self.beatMarkers.clear()

        # Set the maximum time span for the preview
        
        #song_or_preview_length = self.raw_song_length if self.raw_song_length < self.PREVIEW_LENGTH else self.PREVIEW_LENGTH
        max_beats_length = self.PREVIEW_LENGTH - self.song_start_time

        # Calculate the number of beats that can fit within max_beats_length
        number_of_beats = int(max_beats_length / seconds_per_beat)

        # Generate times for beat markers, ensuring they do not exceed max_beats_length
        beat_times = np.arange(
            self.song_start_time,
            self.song_start_time + number_of_beats * seconds_per_beat + self.BEAT_OFFSET,
            seconds_per_beat
        )

        skip_beats = self.skipBeatsBox.value()
        skip_time = skip_beats * seconds_per_beat

        for index, beat_time in enumerate(beat_times):
            actual_index = index - skip_beats
            if actual_index % 16 == 0 and actual_index >= 0:
                width = 3
                new_pen = pg.mkPen((255,86,108,200), width=width)
            elif actual_index % 4 == 0 and actual_index >= 0:
                width = 2
                new_pen = pg.mkPen((255,86,108,150), width=width)
            else:
                width = 1
                new_pen = pg.mkPen((255,86,108,100), width=width)

            marker = pg.InfiniteLine(pos=beat_time, angle=90, pen=new_pen)
            self.graphWidget.addItem(marker)
            self.beatMarkers.append(marker)

        self.update_skip_beats()
            
    def update_skip_beats(self):
        bpm = self.BPMBox.value()
        seconds_per_beat = 60 / bpm
        skip_beats = self.skipBeatsBox.value()
        self.skip_beats = skip_beats

        skip_time = skip_beats * seconds_per_beat
        self.skipBeatsItem.setValue(self.song_start_time + skip_time)


    '''def handle_click(self, event):
        if not self.is_loaded_file:
            return
        if event.button() == Qt.MouseButton.LeftButton:
            click_pos = event.scenePos()
            x_pos = self.graphWidget.getPlotItem().vb.mapSceneToView(click_pos).x()
            if x_pos < 0.0:
                x_pos = 0.0
            elif x_pos > self.PREVIEW_LENGTH:
                x_pos = self.PREVIEW_LENGTH
            self.align_beats_to_click(x_pos)
            self.update_beat_grid()

    def align_beats_to_click(self, click_time):
        bpm = self.BPMBox.value()
        seconds_per_beat = 60 / bpm

        # Calculate the nearest beat time before the click
        nearest_beat_before_click = seconds_per_beat * (click_time // seconds_per_beat)
        
        # Set the offset to align the nearest beat with the click position
        self.BEAT_OFFSET = click_time - nearest_beat_before_click
        self.timeOffsetLabel.setText(str(self.BEAT_OFFSET))
        self.update_beat_grid()

        self.update_start_time(click_time)'''


    def handle_click(self, event):
        if not self.is_loaded_file:
            return
        pos = event.scenePos()
        mouse_point = self.plot_item.vb.mapSceneToView(pos)
        x_pos = mouse_point.x()
        if event.button() == Qt.LeftButton:
            self.align_beats_to_click(x_pos)
        elif event.button() == Qt.RightButton:
            self.adjust_start_position(x_pos)

    def align_beats_to_click(self, click_time):
        bpm = self.BPMBox.value()
        seconds_per_beat = 60 / bpm
        nearest_beat_before_click = seconds_per_beat * (click_time // seconds_per_beat)
        self.BEAT_OFFSET = click_time - nearest_beat_before_click
        self.update_start_time(max(0.0, click_time))
        self.update_beat_grid()

    def adjust_start_position(self, click_time):
        bpm = self.BPMBox.value()
        seconds_per_beat = 60 / bpm
        beat_times = np.arange(
            self.song_start_time,
            self.song_start_time + self.raw_song_length,
            seconds_per_beat
        )
        nearest_beat_index = np.argmin(np.abs(beat_times - click_time))
        nearest_beat_time = beat_times[nearest_beat_index]
        offset = click_time - nearest_beat_time
        self.update_start_time(max(0.0, self.song_start_time + offset))
        self.align_beats_to_click(self.song_start_time)




    def update_start_time(self,_time):
        self.song_start_time = _time
        self.songStartItem.setValue(_time)

    def get_file(self):
        id3tag = None
        result = QFileDialog.getOpenFileName(
            filter="*.ogg *.OGG *.wav *.WAV *.FLAC *.flac *.mp3 *.MP3"
            )
        
        if not result[0]:
            return

        if self.is_loaded_file:
            self.reset_beat_grid(True)
        else:
            self.is_loaded_file = True
            

        self.songNameTextEdit.setText("")
        self.artistNameTextEdit.setText("")
        self.genreTextEdit.setText("")
        self.hypeBox.setValue(5)
        self.feelsBox.setValue(5)
        self.uniqueFilenameTextEdit.setText("")
        self.BEAT_OFFSET = 0.0
        self.timeOffsetLabel.setText("0.0000000")

        try:
            self.update_status("Reading ID3 tags")
            
            
            id3tag = music_tag.load_file(result[0])
            print(id3tag)
            self.id3tag = id3tag
        except Exception as e:
            print(e)
            pass
        
        if id3tag:
            if id3tag['tracktitle']:
                self.songNameTextEdit.setText(str(id3tag['tracktitle']))
            if id3tag['artist']:
                self.artistNameTextEdit.setText(str(id3tag['artist']))
            if id3tag['genre']:
                self.genreTextEdit.setText(str(id3tag['genre']))

            art = None
            try:
                if id3tag['artwork']:
                    art = id3tag['artwork'].first
            except:
                pass
            
        if art:
            pixmap = QPixmap()
            byte_array = QByteArray(art.data)
            buffer = QBuffer(byte_array)
            buffer.open(QBuffer.ReadOnly)
            pixmap.loadFromData(buffer.data(), 'JPEG')  # 'JPEG' is the format of the image

            # Create a QLabel to display the image
            self.album_art = pixmap.scaled(512, 512, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
            self.imageLabel.setPixmap(pixmap.scaled(256, 256, Qt.IgnoreAspectRatio, Qt.SmoothTransformation))
            self.ready = True

            
        self.filenameLabel.setText(result[0])
        self.file_path = result[0]
        sanitised_filepath = os.path.splitext(os.path.split(result[0])[-1])[0]
        self.uniqueFilenameTextEdit.setText(
            sanitised_filepath.replace(" ","_").replace(",","_").replace(".","_")
            )
        
        self.update_status("Reading file data")
        
        raw_data, sr = librosa.load(self.file_path, sr=44100)
        self.raw_data, self.sr = raw_data, sr
        
        raw_song_length = len(raw_data) / sr
        self.raw_song_length = raw_song_length
        
        self.PREVIEW_LENGTH = int(raw_song_length)# if raw_song_length < self.DEFAULT_PREVIEW_LENGTH else self.DEFAULT_PREVIEW_LENGTH
        #self.raw_data, index = librosa.effects.trim(self.raw_data,hop_length=512, frame_length = 512)
        # Print the durations
        #print(len(yt))
        #print(len(self.raw_data))
        self.progressBar.setValue(1)
        self.update_status("Loading {} sec waveform".format(str(self.PREVIEW_LENGTH)))
        
        self.BEAT_OFFSET = 0.0
        self.update_graph(self.raw_data[:self.sr * self.PREVIEW_LENGTH], self.sr)
        

        self.estimate_BPM()
        self.update_beat_grid()
        self.update_status("Song loaded!")
        
        #first_beat = find_first_beat(self.raw_data, self.sr)
        #if first_beat:
        #    print("FIRST BEAT AT", first_beat)
        #    self.graphWidget.addItem(pg.InfiniteLine(pos=first_beat, angle=90, pen=pg.mkPen('g', width=1.5)))
        self.check_ready()

    def estimate_BPM(self):

        if not self.is_loaded_file:
            self.update_status("Load a song first >:(")
            
            return

        self.update_status("Estimating BPM")
        
        
        bpm_result = estimate_bpm(self.raw_data, self.sr)
        
        if bpm_result:
            tempo,beats = bpm_result
            if tempo == self.BPMBox.value():
                self.update_beat_grid()
            else:
                self.BPMBox.setValue(int(tempo))


    def get_album_art(self):
        result = QFileDialog.getOpenFileName(
            filter="*.jpg *.JPG *.png *.PNG *.gif *.GIF"
            )
        if not result[0]:
            return
        self.album_art = QPixmap(result[0]).scaled(512, 512, Qt.IgnoreAspectRatio, Qt.SmoothTransformation)
        self.imageLabel.setPixmap(self.album_art.scaled(256, 256))
        
        self.check_ready()

    def convert_file(self):
        self.update_status("Creating files")
        
        
        folder_path_text = self.uniqueFilenameTextEdit.text()
        folder_path = os.path.join("music",folder_path_text)
        print(folder_path)
        if not os.path.isdir(folder_path):
            os.makedirs(folder_path)
        export_dict = {
            "name": self.songNameTextEdit.text(),
            "artist": self.artistNameTextEdit.text(),
            "genre": self.genreTextEdit.text(),
            "bpm": self.BPMBox.value(),
            "hype": self.hypeBox.value(),
            "feels": self.feelsBox.value(),
            "beat_offset": self.BEAT_OFFSET,
            "start_time": self.song_start_time,
            "skip_beats": self.skip_beats,
            }
        file_template = os.path.join(folder_path,folder_path_text)

        self.album_art.save(file_template + ".jpg", "JPG", 95)
        with open(file_template + ".json","w+") as jsonfile:
            json.dump(export_dict,jsonfile)

        self.update_status("Converting files to .ogg")
        

        if not self.convert_move_ogg(file_template + ".ogg"):
            QMessageBox.critical(self, ".OGG Conversion Error", 
                                 'Failed to convert file. Ensure ffmpeg is available at "this.exe/bin/ffmpeg.exe" \n Also make sure ffmpeg binary is capable of vorbis conversion.', 
                                 QMessageBox.Ok)            
            return
        

        self.update_status("Creating full track waveform preview")
        
        
        self.process_audio_file(folder_path,thumbnail=True)
        
        self.update_status("Creating waveform preview")
        
        
        self.process_audio_file(folder_path,thumbnail=False)
        
        self.progressBar.setValue(100)

        self.update_status("Finished!")
        

    def check_ready(self):
        if self.album_art and self.file_path:
            self.ready = True
        self.convertBtn.setEnabled(self.ready)

    def convert_move_ogg(self, output_path):
        try:
            # Check if audio is stereo and process accordingly
            if self.raw_data.ndim > 1:  # Stereo
                max_val = np.max(np.abs(self.raw_data))  # Find max absolute value for normalization
                channels = [AudioSegment(
                                data=np.int16(self.raw_data[channel] / max_val * 32767).tobytes(),
                                sample_width=2,
                                frame_rate=self.sr,
                                channels=1)
                            for channel in range(self.raw_data.shape[0])]
                sound = AudioSegment.from_mono_audiosegments(*channels)
            else:  # Mono
                max_val = np.max(np.abs(self.raw_data))  # Find max absolute value for normalization
                data = np.int16(self.raw_data / max_val * 32767).tobytes()
                sound = AudioSegment(data=data, sample_width=2, frame_rate=self.sr, channels=1)

            # Export to OGG, using the original sample rate
            sound.export(output_path, format='ogg', bitrate="192k")
            print("File saved successfully to:", output_path)
        except Exception as e:
            print("EXCEPTION,", e)
            return False
        return True


    def process_audio_file(self,audio_path,output_path="music",thumbnail=False):
        
        self.progressBar.setValue(10)
        input_filename = os.path.split(audio_path)[-1]
        if output_path: # if output folder is declared, it will create folder for everything else plop all next to script
            output_path = os.path.join(output_path,input_filename)
            if not os.path.isdir(output_path):
                os.makedirs(output_path)

        waveform_mask_path = 'waveform_mask.png'
        frequency_color_map_path = 'frequency_color_map.png'
        
        # load audio

        raw_data = self.raw_data
        sr = self.sr

        if thumbnail:
            raw_data = self.raw_data[::10]
            sr = self.sr / 10
        else:
            if self.qualityCombo.currentIndex() == 0: # fast
                raw_data = self.raw_data[::2]
                sr = int(self.sr / 2)
            else:
                print(self.qualityCombo.currentIndex())
                pass

        # duration of each chunk in seconds
        chunk_duration = 25  # 25 seconds

        # samples per chunk
        samples_per_chunk = sr * chunk_duration

        # total number of samples in the audio file
        total_samples = len(raw_data)

        # pixels per second for visualization
        pixels_per_second = 640  # Adjust this value as needed

        output_images = []

        if thumbnail:
            samples_per_chunk = total_samples

        # Create a single figure and axis to reuse for frequency plotting
        fig_freq, ax_freq = plt.subplots(figsize=(16, 1))
        ax_freq.axis('off')  # Turn off axis


        # Process each chunk
        for indx, start in enumerate(range(0, total_samples, samples_per_chunk)):
            end = start + samples_per_chunk
            if end > total_samples:
                end = total_samples
            data = raw_data[start:end]

            # Calculate the completion percentage
            progress_percentage = int((end / total_samples) * 100)

            # Update the progress bar
            if not thumbnail:
                self.progressBar.setValue(progress_percentage - 1)
                QApplication.processEvents()

            # Actual duration of the chunk in seconds
            actual_duration = (end - start) / sr
            if thumbnail:
                image_width = 958
            else:
                image_width = int(pixels_per_second * actual_duration)  # Calculate the dynamic width based on actual chunk duration

            if len(data.shape) > 1:
                data = data[:, 0]  # Mono conversion if stereo

            time = np.linspace(0., actual_duration, data.shape[0])
            normalized_data = data / np.max(np.abs(data), axis=0)

            #print("waveforrm mask plot")

            # Plotting the waveform
            fig, ax = plt.subplots(figsize=(image_width / 100, 1))  # Width and height in inches
            ax.plot(time, normalized_data, color='black')
            ax.fill_between(time, normalized_data, color='black')
            ax.axis('off')  # Turn off axis

            ax.set_xlim(time[0], time[-1])

            # Remove padding and margins
            fig.subplots_adjust(left=0, right=1, top=1, bottom=0)

            # Save the mask
            print("saving waveforrm mask plot")
            plt.savefig(waveform_mask_path, dpi=100, bbox_inches='tight', pad_inches=0)  # 16000x100 pixels
            #print("saved mask plot, closing")
            plt.close()
            #print("closed mask plot")

            
            QApplication.processEvents()

            #print("computing short time fft")
            # Compute the Short-Time Fourier Transform (STFT)
            n_fft = 2048
            hop_length = 512
            D = np.abs(librosa.stft(data, n_fft=n_fft, hop_length=hop_length))
            frequencies = librosa.fft_frequencies(sr=sr, n_fft=n_fft)

            # Frequency bands definitions
            bands = [0, 20, 60, 100, 200, 500, sr/2]  # Up to Nyquist frequency
            band_colors = ['purple', 'purple', 'deeppink', 'red', 'green', 'blue', 'indigo']  # Corresponding colors

            # Create a color mapping based on energy in each band
            #print("creating spectrum")
            spectrogram = np.zeros((len(bands) - 1, D.shape[1]), dtype=int)
            #print("calculating band data for spectrogram")
            for i in range(1, len(bands)):
                band_mask = (frequencies >= bands[i-1]) & (frequencies < bands[i])
                band_energy = np.sum(D[band_mask, :]**2, axis=0)
                spectrogram[i-1, :] = band_energy
            #print("normalising spectogram")
            norm_spectrogram = spectrogram / np.max(spectrogram, axis=0)
            #print("creating image data")
            img_data = np.zeros((1, D.shape[1], 3), dtype=float)
            for i, color in enumerate(band_colors[:-1]):
                #print(f"processing band {i} {color}")
                color_rgb = to_rgb(color)
                img_data[:, :, 0] += norm_spectrogram[i, :] * color_rgb[0]
                img_data[:, :, 1] += norm_spectrogram[i, :] * color_rgb[1]
                img_data[:, :, 2] += norm_spectrogram[i, :] * color_rgb[2]

            #print("plotting")


            # Plotting the frequency color mapping
            fig, ax = plt.subplots(figsize=(image_width / 100, 1))  # Width and height in inches
            ax.imshow(img_data, aspect='auto')
            ax.axis('off')
            #ax.set_xlim(time[0], time[-1])
            fig.subplots_adjust(left=0, right=1, top=1, bottom=0)
            #print("saving freq plot")
            plt.savefig(frequency_color_map_path, dpi=100, bbox_inches='tight', pad_inches=0)
            plt.close()

            QApplication.processEvents()
            #print("making final plot")
            # Masking and final image creation
            mask = Image.open(waveform_mask_path).convert('L')  # Convert mask to grayscale
            
            mask = Image.eval(mask, lambda x: 255 - x)  # Invert mask
            frequency_image = Image.open(frequency_color_map_path).convert('RGBA')
            result_image = Image.new('RGBA', frequency_image.size, (0, 0, 0, 0))

            # Paste the frequency image onto the result image, using the mask to control the transparency
            result_image.paste(frequency_image, (0, 0), mask)

            indx_or_thumb_str = f"{indx}"
            if thumbnail:
                indx_or_thumb_str = "preview"
            # Save the combined image for each chunk
            output_image_path = f'{output_path}/{input_filename}_wf_{indx_or_thumb_str}.png'
            output_images.append(output_image_path)
            result_image.save(output_image_path)

        bin_list = [frequency_color_map_path, waveform_mask_path]
        for file in bin_list:
            os.remove(file)




def estimate_bpm(samps, fs):
    # Minimum duration for accurate BPM estimation (in seconds)
    min_duration = 7.0

    if len(samps) / fs < min_duration:
        print("Audio duration is too short for BPM estimation.")
        return None

    # Apply a low-pass filter to reduce high-frequency noise
    #samps_filtered = low_pass_filter(samps, fs, cutoff=220)

    # Compute the beats using librosa's beat.beat_track
    print("1")
    onset_env = librosa.onset.onset_strength(y=samps, sr=fs)
    pulse = librosa.beat.plp(onset_envelope=onset_env, sr=fs)
    print("2")
    tempo, beats = librosa.beat.beat_track(
        onset_envelope=pulse,
        sr=fs,
        units='frames',
        trim=True,
        tightness=1.0
    )

    if tempo <= 0:
        print("BPM estimation failed.")
        return None

    tempo = adjust_tempo(tempo)

    return tempo, beats

def adjust_tempo(tempo):
    # Round to nearest 0.5
    rounded_tempo = np.floor(tempo)#int(tempo * 2) / 2
    print(f"original tempo: {tempo}\nrounded tempo: {rounded_tempo}")

    if rounded_tempo < 90:
        print(f"doubled tempo: {rounded_tempo}")
        return np.ceil(rounded_tempo * 2)
    else:
        return int(rounded_tempo)

def find_first_beat(raw_audio, sr, full=False):
    # Track beats
    tempo, beats = librosa.beat.beat_track(y=raw_audio, sr=sr)
    
    # Convert the beat frames to timestamps
    beat_times = librosa.frames_to_time(beats, sr=sr)
    
    if beat_times.size > 0:
        first_beat_time = beat_times[0]
        print(f"First beat at: {first_beat_time:.2f} seconds")
        if not full:
            return first_beat_time
        else:
            return beat_times
    else:
        print("No beats detected.")
        return None


if __name__ == '__main__':
    ui = MainWindow()
    ui.show()
    sys.exit(app.exec_())
