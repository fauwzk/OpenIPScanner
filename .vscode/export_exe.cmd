@echo off
rmdir /s /q build
rmdir /s /q dist
rmdir /s /q output
python -m black src\*.py
pyinstaller --noconfirm --onefile --console --name "OpenIPScanner" "src\main.py"
ren dist output
rmdir /s /q build
