@echo off
rmdir /s /q dist
pyinstaller --noconfirm --onefile --console --name "OpenIPScanner" "src\main.py"
rmdir /s /q build
