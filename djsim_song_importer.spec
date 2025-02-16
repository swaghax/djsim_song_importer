# -*- mode: python ; coding: utf-8 -*-
#>python -m PyInstaller djsim_song_importer.spec

a = Analysis(
    ['djsim_song_importer.py'],
    pathex=[],
    binaries=[],
    datas=[
        ],
    hiddenimports=['secrets'],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'tkinter',
        'hdf5',
        'h5py',
        'MySQLdb',
        #'scipy',
        'Qt5DBus',
        'Qt5Quick',
        'Qt5WebSockets',
        'Qt5VirtualKeyboard',
        'Qt5Test',
        'Qt5OpenGL',
        'sciplibGLESv2y',
        'libEGL',
        #'multiprocessing',
        #'Cython',
        'sklearn',
        'cryptography',
        'pandas',
        'pytz',
        'OpenSSL',
        'urllib3',
        'requests',
        'bs4',
        'sqlalchemy',
        'greenlet',
        'sqlite3',
        'tqdm',
        'pooch',
        #'numba',
        'pythoncom',
        'win32com',
        'yaml',
        #'llvmlite',
        #'pygments',
        'tomli',
        'pluggy',
        'jinja2',
        'psutil',
        #'asyncio',
        #'concurrent.futures',
        ],
    noarchive=False,
    optimize=0,
)
pyz = PYZ(a.pure)


Key = [
    'PySide2\\Qt5DBus.dll',
    'PySide2\\libEGL.dll',
    'PySide2\\opengl32sw.dll',
    'PySide2\\d3dcompiler_47.dll',
    'PySide2\\Qt5Pdf.dll',
    #'PySide2\\Qt5Network.dll', # need these apparently
    #'PySide2\\Qt5Qml.dll', # need these apparently
    'PySide2\\Qt5QmlModels.dll',
    'PySide2\\Qt5Svg.dll',
    'PySide2\\Qt5Quick.dll', 
    'PySide2\\Qt5WebSockets.dll',
    'PySide2\\Qt5VirtualKeyboard.dll', # not this
    'PySide2\\libGLESv2.dll',
    'PySide2\\plugins\\platforms\\qwebgl.dll',
    'PySide2\\plugins\\imageformats\\qwebp.dll',
    'PySide2\\plugins\\imageformats\\qtiff.dll',
    'PySide2\\plugins\\imageformats\\qsvg',
    'PySide2\\plugins\\imageformats\\qpdf.dll',
    'PySide2\\plugins\\iconengines\\qsvgicon.dll',
    ]


def remove_from_list(input, keys):
    outlist = []
    for item in input:
        name, _, _ = item
        flag = 0
        for key_word in keys:
            if name.find(key_word) > -1:
                flag = 1
        if flag != 1:
            outlist.append(item)
    return outlist

a.binaries = remove_from_list(a.binaries, Key)



exe = EXE(
    pyz,
    a.scripts,
    a.binaries,
    a.datas,
    [],
    name='djsim_song_importer',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    #upx_exclude=['Qt5Core.dll', 'Qt5Gui.dll', 'Qt5Widgets.dll'],
    runtime_tmpdir=None,
    console=False,
    icon = 'dj_sim_ico.ico',
    disable_windowed_traceback=False,
    argv_emulation=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
)
