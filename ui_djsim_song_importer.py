# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'djsim_song_importernpKCBY.ui'
##
## Created by: Qt User Interface Compiler version 5.14.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import (QCoreApplication, QDate, QDateTime, QMetaObject,
    QObject, QPoint, QRect, QSize, QTime, QUrl, Qt)
from PySide2.QtGui import (QBrush, QColor, QConicalGradient, QCursor, QFont,
    QFontDatabase, QIcon, QKeySequence, QLinearGradient, QPalette, QPainter,
    QPixmap, QRadialGradient)
from PySide2.QtWidgets import *

from pyqtgraph import PlotWidget

import resources_rc

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(622, 565)
        MainWindow.setMaximumSize(QSize(99999, 99999))
        palette = QPalette()
        brush = QBrush(QColor(0, 182, 117, 255))
        brush.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.WindowText, brush)
        brush1 = QBrush(QColor(230, 230, 230, 255))
        brush1.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Button, brush1)
        brush2 = QBrush(QColor(59, 79, 94, 255))
        brush2.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Light, brush2)
        brush3 = QBrush(QColor(15, 22, 26, 255))
        brush3.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Dark, brush3)
        brush4 = QBrush(QColor(0, 0, 0, 255))
        brush4.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Text, brush4)
        brush5 = QBrush(QColor(255, 255, 255, 255))
        brush5.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.BrightText, brush5)
        brush6 = QBrush(QColor(191, 0, 201, 255))
        brush6.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.ButtonText, brush6)
        palette.setBrush(QPalette.Active, QPalette.Base, brush5)
        brush7 = QBrush(QColor(28, 37, 44, 255))
        brush7.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Window, brush7)
        brush8 = QBrush(QColor(255, 86, 108, 255))
        brush8.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Active, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Active, QPalette.HighlightedText, brush4)
        brush9 = QBrush(QColor(255, 255, 255, 128))
        brush9.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Active, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Inactive, QPalette.WindowText, brush)
        palette.setBrush(QPalette.Inactive, QPalette.Button, brush1)
        palette.setBrush(QPalette.Inactive, QPalette.Light, brush2)
        palette.setBrush(QPalette.Inactive, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Inactive, QPalette.Text, brush4)
        palette.setBrush(QPalette.Inactive, QPalette.BrightText, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.ButtonText, brush6)
        palette.setBrush(QPalette.Inactive, QPalette.Base, brush5)
        palette.setBrush(QPalette.Inactive, QPalette.Window, brush7)
        palette.setBrush(QPalette.Inactive, QPalette.Highlight, brush8)
        palette.setBrush(QPalette.Inactive, QPalette.HighlightedText, brush4)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush9)
#endif
        palette.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Button, brush1)
        palette.setBrush(QPalette.Disabled, QPalette.Light, brush2)
        palette.setBrush(QPalette.Disabled, QPalette.Dark, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Text, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.BrightText, brush5)
        palette.setBrush(QPalette.Disabled, QPalette.ButtonText, brush3)
        palette.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        palette.setBrush(QPalette.Disabled, QPalette.Window, brush7)
        brush10 = QBrush(QColor(0, 120, 215, 255))
        brush10.setStyle(Qt.SolidPattern)
        palette.setBrush(QPalette.Disabled, QPalette.Highlight, brush10)
        palette.setBrush(QPalette.Disabled, QPalette.HighlightedText, brush4)
        brush11 = QBrush(QColor(0, 0, 0, 128))
        brush11.setStyle(Qt.SolidPattern)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush11)
#endif
        MainWindow.setPalette(palette)
        font = QFont()
        font.setPointSize(10)
        MainWindow.setFont(font)
        icon = QIcon()
        icon.addFile(u":/images/dj_sim_ico.ico", QSize(), QIcon.Normal, QIcon.Off)
        MainWindow.setWindowIcon(icon)
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.verticalLayout_2 = QVBoxLayout(self.centralwidget)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.horizontalLayout_16.setContentsMargins(-1, 0, -1, -1)
        self.loadFileBtn = QPushButton(self.centralwidget)
        self.loadFileBtn.setObjectName(u"loadFileBtn")
        sizePolicy = QSizePolicy(QSizePolicy.Minimum, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.loadFileBtn.sizePolicy().hasHeightForWidth())
        self.loadFileBtn.setSizePolicy(sizePolicy)
        self.loadFileBtn.setMinimumSize(QSize(283, 0))
        self.loadFileBtn.setMaximumSize(QSize(283, 16777215))

        self.horizontalLayout_16.addWidget(self.loadFileBtn)

        self.filenameLabel = QLineEdit(self.centralwidget)
        self.filenameLabel.setObjectName(u"filenameLabel")
        self.filenameLabel.setEnabled(False)
        palette1 = QPalette()
        palette1.setBrush(QPalette.Active, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Active, QPalette.Base, brush7)
        brush12 = QBrush(QColor(191, 0, 201, 128))
        brush12.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Active, QPalette.PlaceholderText, brush12)
#endif
        palette1.setBrush(QPalette.Inactive, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Inactive, QPalette.Base, brush7)
        brush13 = QBrush(QColor(191, 0, 201, 128))
        brush13.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Inactive, QPalette.PlaceholderText, brush13)
#endif
        palette1.setBrush(QPalette.Disabled, QPalette.Text, brush6)
        palette1.setBrush(QPalette.Disabled, QPalette.Base, brush7)
        brush14 = QBrush(QColor(191, 0, 201, 128))
        brush14.setStyle(Qt.NoBrush)
#if QT_VERSION >= QT_VERSION_CHECK(5, 12, 0)
        palette1.setBrush(QPalette.Disabled, QPalette.PlaceholderText, brush14)
#endif
        self.filenameLabel.setPalette(palette1)
        font1 = QFont()
        font1.setItalic(True)
        self.filenameLabel.setFont(font1)
        self.filenameLabel.setFrame(False)
        self.filenameLabel.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)
        self.filenameLabel.setReadOnly(True)

        self.horizontalLayout_16.addWidget(self.filenameLabel)


        self.verticalLayout.addLayout(self.horizontalLayout_16)

        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.verticalLayout_6.setContentsMargins(-1, -1, 0, -1)
        self.frame = QFrame(self.centralwidget)
        self.frame.setObjectName(u"frame")
        sizePolicy1 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.frame.sizePolicy().hasHeightForWidth())
        self.frame.setSizePolicy(sizePolicy1)
        self.frame.setMinimumSize(QSize(280, 280))
        self.frame.setMaximumSize(QSize(999, 280))
        self.frame.setFrameShape(QFrame.Box)
        self.frame.setFrameShadow(QFrame.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.imageLabel = QLabel(self.frame)
        self.imageLabel.setObjectName(u"imageLabel")
        sizePolicy2 = QSizePolicy(QSizePolicy.Preferred, QSizePolicy.Preferred)
        sizePolicy2.setHorizontalStretch(1)
        sizePolicy2.setVerticalStretch(1)
        sizePolicy2.setHeightForWidth(self.imageLabel.sizePolicy().hasHeightForWidth())
        self.imageLabel.setSizePolicy(sizePolicy2)
        self.imageLabel.setMinimumSize(QSize(256, 256))
        self.imageLabel.setMaximumSize(QSize(256, 256))

        self.verticalLayout_5.addWidget(self.imageLabel)

        self.loadImageBtn = QPushButton(self.frame)
        self.loadImageBtn.setObjectName(u"loadImageBtn")
        self.loadImageBtn.setMaximumSize(QSize(80, 16777215))

        self.verticalLayout_5.addWidget(self.loadImageBtn)


        self.verticalLayout_6.addWidget(self.frame)


        self.horizontalLayout_3.addLayout(self.verticalLayout_6)

        self.verticalLayout_4 = QVBoxLayout()
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setSpacing(0)
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.horizontalLayout_5.setContentsMargins(-1, 0, -1, -1)
        self.label_5 = QLabel(self.centralwidget)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_5.addWidget(self.label_5)

        self.uniqueFilenameTextEdit = QLineEdit(self.centralwidget)
        self.uniqueFilenameTextEdit.setObjectName(u"uniqueFilenameTextEdit")
        self.uniqueFilenameTextEdit.setMinimumSize(QSize(202, 0))
        self.uniqueFilenameTextEdit.setMaximumSize(QSize(200, 16777215))
        self.uniqueFilenameTextEdit.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_5.addWidget(self.uniqueFilenameTextEdit)

        self.horizontalSpacer_2 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_5.addItem(self.horizontalSpacer_2)


        self.verticalLayout_4.addLayout(self.horizontalLayout_5)

        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setSpacing(0)
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.horizontalLayout_9.setContentsMargins(-1, 0, -1, -1)
        self.label_6 = QLabel(self.centralwidget)
        self.label_6.setObjectName(u"label_6")
        self.label_6.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_9.addWidget(self.label_6)

        self.songNameTextEdit = QLineEdit(self.centralwidget)
        self.songNameTextEdit.setObjectName(u"songNameTextEdit")
        sizePolicy3 = QSizePolicy(QSizePolicy.MinimumExpanding, QSizePolicy.Fixed)
        sizePolicy3.setHorizontalStretch(0)
        sizePolicy3.setVerticalStretch(0)
        sizePolicy3.setHeightForWidth(self.songNameTextEdit.sizePolicy().hasHeightForWidth())
        self.songNameTextEdit.setSizePolicy(sizePolicy3)
        self.songNameTextEdit.setMinimumSize(QSize(202, 0))
        self.songNameTextEdit.setMaximumSize(QSize(200, 16777215))
        self.songNameTextEdit.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_9.addWidget(self.songNameTextEdit)

        self.horizontalSpacer_3 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_9.addItem(self.horizontalSpacer_3)


        self.verticalLayout_4.addLayout(self.horizontalLayout_9)

        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setSpacing(0)
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.horizontalLayout_11.setContentsMargins(-1, 0, -1, -1)
        self.label_8 = QLabel(self.centralwidget)
        self.label_8.setObjectName(u"label_8")
        self.label_8.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_11.addWidget(self.label_8)

        self.artistNameTextEdit = QLineEdit(self.centralwidget)
        self.artistNameTextEdit.setObjectName(u"artistNameTextEdit")
        sizePolicy3.setHeightForWidth(self.artistNameTextEdit.sizePolicy().hasHeightForWidth())
        self.artistNameTextEdit.setSizePolicy(sizePolicy3)
        self.artistNameTextEdit.setMinimumSize(QSize(202, 0))
        self.artistNameTextEdit.setMaximumSize(QSize(200, 16777215))
        self.artistNameTextEdit.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_11.addWidget(self.artistNameTextEdit)

        self.horizontalSpacer_4 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_11.addItem(self.horizontalSpacer_4)


        self.verticalLayout_4.addLayout(self.horizontalLayout_11)

        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setSpacing(0)
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.horizontalLayout_10.setContentsMargins(-1, 0, -1, -1)
        self.label_7 = QLabel(self.centralwidget)
        self.label_7.setObjectName(u"label_7")
        self.label_7.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_10.addWidget(self.label_7)

        self.genreTextEdit = QLineEdit(self.centralwidget)
        self.genreTextEdit.setObjectName(u"genreTextEdit")
        self.genreTextEdit.setMinimumSize(QSize(202, 0))
        self.genreTextEdit.setMaximumSize(QSize(200, 16777215))
        self.genreTextEdit.setInputMethodHints(Qt.ImhNone)

        self.horizontalLayout_10.addWidget(self.genreTextEdit)

        self.horizontalSpacer_5 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_10.addItem(self.horizontalSpacer_5)


        self.verticalLayout_4.addLayout(self.horizontalLayout_10)

        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setSpacing(2)
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_3 = QLabel(self.centralwidget)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_8.addWidget(self.label_3)

        self.hypeBox = QSpinBox(self.centralwidget)
        self.hypeBox.setObjectName(u"hypeBox")
        self.hypeBox.setMinimumSize(QSize(50, 0))
        self.hypeBox.setMaximumSize(QSize(50, 16777215))
        self.hypeBox.setMaximum(10)
        self.hypeBox.setValue(5)

        self.horizontalLayout_8.addWidget(self.hypeBox)

        self.label_2 = QLabel(self.centralwidget)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_8.addWidget(self.label_2)

        self.feelsBox = QSpinBox(self.centralwidget)
        self.feelsBox.setObjectName(u"feelsBox")
        self.feelsBox.setMinimumSize(QSize(50, 0))
        self.feelsBox.setMaximumSize(QSize(50, 16777215))
        self.feelsBox.setMaximum(10)
        self.feelsBox.setValue(5)

        self.horizontalLayout_8.addWidget(self.feelsBox)

        self.label_4 = QLabel(self.centralwidget)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setMaximumSize(QSize(50, 16777215))

        self.horizontalLayout_8.addWidget(self.label_4)

        self.BPMBox = QSpinBox(self.centralwidget)
        self.BPMBox.setObjectName(u"BPMBox")
        self.BPMBox.setMinimumSize(QSize(50, 0))
        self.BPMBox.setMaximumSize(QSize(50, 16777215))
        self.BPMBox.setMinimum(30)
        self.BPMBox.setMaximum(300)
        self.BPMBox.setValue(130)

        self.horizontalLayout_8.addWidget(self.BPMBox)

        self.analyseBPMBtn = QToolButton(self.centralwidget)
        self.analyseBPMBtn.setObjectName(u"analyseBPMBtn")

        self.horizontalLayout_8.addWidget(self.analyseBPMBtn)

        self.horizontalSpacer_6 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_8.addItem(self.horizontalSpacer_6)


        self.verticalLayout_4.addLayout(self.horizontalLayout_8)

        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.label = QLabel(self.centralwidget)
        self.label.setObjectName(u"label")
        self.label.setMinimumSize(QSize(100, 0))
        self.label.setAlignment(Qt.AlignLeading|Qt.AlignLeft|Qt.AlignVCenter)

        self.horizontalLayout_6.addWidget(self.label)

        self.qualityCombo = QComboBox(self.centralwidget)
        self.qualityCombo.addItem("")
        self.qualityCombo.addItem("")
        self.qualityCombo.setObjectName(u"qualityCombo")
        self.qualityCombo.setMinimumSize(QSize(196, 0))
        self.qualityCombo.setMaximumSize(QSize(120, 16777215))

        self.horizontalLayout_6.addWidget(self.qualityCombo)

        self.horizontalSpacer_8 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_6.addItem(self.horizontalSpacer_8)


        self.verticalLayout_4.addLayout(self.horizontalLayout_6)

        self.label_10 = QLabel(self.centralwidget)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setEnabled(True)
        sizePolicy1.setHeightForWidth(self.label_10.sizePolicy().hasHeightForWidth())
        self.label_10.setSizePolicy(sizePolicy1)
        palette2 = QPalette()
        palette2.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        palette2.setBrush(QPalette.Disabled, QPalette.WindowText, brush3)
        self.label_10.setPalette(palette2)
        self.label_10.setInputMethodHints(Qt.ImhMultiLine)
        self.label_10.setAlignment(Qt.AlignBottom|Qt.AlignLeading|Qt.AlignLeft)
        self.label_10.setWordWrap(False)
        self.label_10.setMargin(0)

        self.verticalLayout_4.addWidget(self.label_10)


        self.horizontalLayout_3.addLayout(self.verticalLayout_4)


        self.verticalLayout.addLayout(self.horizontalLayout_3)

        self.frame_2 = QFrame(self.centralwidget)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setMinimumSize(QSize(0, 50))
        self.frame_2.setFrameShape(QFrame.Box)
        self.frame_2.setFrameShadow(QFrame.Sunken)
        self.verticalLayout_7 = QVBoxLayout(self.frame_2)
        self.verticalLayout_7.setSpacing(0)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.graphWidget = PlotWidget(self.frame_2)
        self.graphWidget.setObjectName(u"graphWidget")
        sizePolicy4 = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.MinimumExpanding)
        sizePolicy4.setHorizontalStretch(0)
        sizePolicy4.setVerticalStretch(0)
        sizePolicy4.setHeightForWidth(self.graphWidget.sizePolicy().hasHeightForWidth())
        self.graphWidget.setSizePolicy(sizePolicy4)
        self.graphWidget.setMinimumSize(QSize(0, 0))

        self.verticalLayout_7.addWidget(self.graphWidget)


        self.verticalLayout.addWidget(self.frame_2)

        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.horizontalLayout_4.setContentsMargins(-1, 0, -1, -1)
        self.offsetResetBtn = QToolButton(self.centralwidget)
        self.offsetResetBtn.setObjectName(u"offsetResetBtn")

        self.horizontalLayout_4.addWidget(self.offsetResetBtn)

        self.label_9 = QLabel(self.centralwidget)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setMinimumSize(QSize(150, 0))

        self.horizontalLayout_4.addWidget(self.label_9)

        self.timeOffsetLabel = QLabel(self.centralwidget)
        self.timeOffsetLabel.setObjectName(u"timeOffsetLabel")

        self.horizontalLayout_4.addWidget(self.timeOffsetLabel)

        self.horizontalSpacer_7 = QSpacerItem(40, 20, QSizePolicy.Expanding, QSizePolicy.Minimum)

        self.horizontalLayout_4.addItem(self.horizontalSpacer_7)

        self.label_11 = QLabel(self.centralwidget)
        self.label_11.setObjectName(u"label_11")

        self.horizontalLayout_4.addWidget(self.label_11)

        self.skipBeatsBox = QSpinBox(self.centralwidget)
        self.skipBeatsBox.setObjectName(u"skipBeatsBox")
        self.skipBeatsBox.setMinimumSize(QSize(50, 0))
        self.skipBeatsBox.setMaximum(99999)

        self.horizontalLayout_4.addWidget(self.skipBeatsBox)


        self.verticalLayout.addLayout(self.horizontalLayout_4)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setSizeConstraint(QLayout.SetDefaultConstraint)
        self.progressBar = QProgressBar(self.centralwidget)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(0)

        self.horizontalLayout_2.addWidget(self.progressBar)

        self.convertBtn = QPushButton(self.centralwidget)
        self.convertBtn.setObjectName(u"convertBtn")
        self.convertBtn.setEnabled(False)
        self.convertBtn.setMinimumSize(QSize(100, 0))

        self.horizontalLayout_2.addWidget(self.convertBtn)


        self.verticalLayout.addLayout(self.horizontalLayout_2)


        self.verticalLayout_2.addLayout(self.verticalLayout)

        MainWindow.setCentralWidget(self.centralwidget)
        self.statusBar = QStatusBar(MainWindow)
        self.statusBar.setObjectName(u"statusBar")
        palette3 = QPalette()
        palette3.setBrush(QPalette.Active, QPalette.WindowText, brush6)
        palette3.setBrush(QPalette.Inactive, QPalette.WindowText, brush6)
        brush15 = QBrush(QColor(120, 120, 120, 255))
        brush15.setStyle(Qt.SolidPattern)
        palette3.setBrush(QPalette.Disabled, QPalette.WindowText, brush15)
        self.statusBar.setPalette(palette3)
        MainWindow.setStatusBar(self.statusBar)

        self.retranslateUi(MainWindow)

        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"DJ SIMULATOR Custom Audio Importer", None))
        self.loadFileBtn.setText(QCoreApplication.translate("MainWindow", u"Load File", None))
        self.filenameLabel.setText(QCoreApplication.translate("MainWindow", u"Load a file to start", None))
        self.imageLabel.setText("")
        self.loadImageBtn.setText(QCoreApplication.translate("MainWindow", u"Load Image", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Unique filename", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Song name", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"Artist name", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Genre", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"Hype", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Feels", None))
        self.label_4.setText(QCoreApplication.translate("MainWindow", u"BPM", None))
        self.analyseBPMBtn.setText(QCoreApplication.translate("MainWindow", u"Analyze", None))
        self.label.setText(QCoreApplication.translate("MainWindow", u"Quality (speed)", None))
        self.qualityCombo.setItemText(0, QCoreApplication.translate("MainWindow", u"Half (Fast)", None))
        self.qualityCombo.setItemText(1, QCoreApplication.translate("MainWindow", u"Full (2x Slower)", None))

        self.label_10.setText(QCoreApplication.translate("MainWindow", u"<html><head/><body><p><span style=\" font-size:9pt;\">Left click below to select start point.</span></p><p><span style=\" font-size:9pt;\">Right click to realign grid / start point.</span></p><p><span style=\" font-size:9pt;\">Hold Left click to pan and scroll to zoom. </span></p></body></html>", None))
        self.offsetResetBtn.setText(QCoreApplication.translate("MainWindow", u"Reset", None))
        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Beat Grid Offset (sec):", None))
        self.timeOffsetLabel.setText(QCoreApplication.translate("MainWindow", u"0.0000", None))
        self.label_11.setText(QCoreApplication.translate("MainWindow", u"Skip beats: ", None))
        self.convertBtn.setText(QCoreApplication.translate("MainWindow", u"Import Song", None))
    # retranslateUi

