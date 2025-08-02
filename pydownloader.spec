# -*- mode: python ; coding: utf-8 -*-
import os
import platform

block_cipher = None

# Dynamically build binaries list based on what exists
binaries = []
datas = []

# Check for existing binaries and add them
if os.path.exists('assets/ffmpeg.exe'):
    binaries.append(('assets/ffmpeg.exe', 'assets/'))
if os.path.exists('assets/ffmpeg'):
    binaries.append(('assets/ffmpeg', 'assets/'))
if os.path.exists('assets/aria2c.exe'):
    binaries.append(('assets/aria2c.exe', 'assets/'))
if os.path.exists('assets/aria2c'):
    binaries.append(('assets/aria2c', 'assets/'))

# Add assets folder if it exists
if os.path.exists('assets/'):
    datas.append(('assets/', 'assets/'))

a = Analysis(
    ['pydownloader.py'],
    pathex=[],
    binaries=binaries,
    datas=datas,
    hiddenimports=[
        'customtkinter',
        'yt_dlp',
        'PIL',
        'PIL._tkinter_finder',
        'tkinter',
        'tkinter.filedialog',
        'tkinter.messagebox',
        'threading',
        'subprocess',
        'platform',
        'uuid',
        'packaging',
        'packaging.version',
        'packaging.specifiers',
        'packaging.requirements',
        'requests',
        'urllib3',
        'certifi',
        'charset_normalizer',
        'idna',
    ],
    hookspath=[],
    hooksconfig={},
    runtime_hooks=[],
    excludes=[
        'matplotlib',
        'numpy',
        'scipy',
        'pandas',
        'jupyter',
        'IPython',
        'notebook',
        'qtpy',
        'PyQt5',
        'PyQt6',
        'PySide2',
        'PySide6',
    ],
    win_no_prefer_redirects=False,
    win_private_assemblies=False,
    cipher=block_cipher,
    noarchive=False,
)

pyz = PYZ(a.pure, a.zipped_data, cipher=block_cipher)

exe = EXE(
    pyz,
    a.scripts,
    [],
    exclude_binaries=True,
    name='PyDownloader',
    debug=False,
    bootloader_ignore_signals=False,
    strip=False,
    upx=True,
    console=False,  # Set to True for debugging
    disable_windowed_traceback=False,
    target_arch=None,
    codesign_identity=None,
    entitlements_file=None,
    icon='assets/icon.ico',  # Add your icon file
)

coll = COLLECT(
    exe,
    a.binaries,
    a.zipfiles,
    a.datas,
    strip=False,
    upx=True,
    upx_exclude=[],
    name='PyDownloader'
)
    