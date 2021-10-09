# -*- mode: python ; coding: utf-8 -*-

import glob

block_cipher = None


a = Analysis(['__init__.py'],
             pathex=['C:\\Users\\Andrés\\Documents\\Python\\SPLRefresher'],
             binaries=[],
             datas=[],
             hiddenimports=[],
             hookspath=[],
             hooksconfig={},
             runtime_hooks=[],
             excludes=[],
             win_no_prefer_redirects=False,
             win_private_assemblies=False,
             cipher=block_cipher,
             noarchive=False)
pyz = PYZ(a.pure, a.zipped_data,
             cipher=block_cipher)

a.datas += [("assets\\"+file.split("\\")[-1], file, "DATA") for file in glob.glob(".\\assets\\*")]

exe = EXE(pyz,
          a.scripts,
          a.binaries,
          a.zipfiles,
          a.datas,  
          [],
          name='__init__',
          debug=False,
          bootloader_ignore_signals=False,
          strip=False,
          upx=True,
          upx_exclude=[],
          runtime_tmpdir=None,
          console=False,
          disable_windowed_traceback=False,
          target_arch=None,
          codesign_identity=None,
          entitlements_file=None,
          icon='.\\assets\\SPLREFRESHER.ICO')
