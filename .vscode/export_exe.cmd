@echo off
rmdir /s /q dist
pyinstaller --noconfirm --onefile --console --name "OpenIPScanner" --add-data "src\nettools.py;."  "src\main.py"
rmdir /s /q build
