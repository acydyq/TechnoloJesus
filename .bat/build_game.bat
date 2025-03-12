@echo off
echo Building TechnoloJesus...

:: Define root directory
set ROOT=C:\Users\Shadow\Documents\.PROJECTS\TechnoloJesus
set BUILD_DIR=%ROOT%\build

:: Clean previous builds
if exist "%BUILD_DIR%\TechnoloJesus.exe" del "%BUILD_DIR%\TechnoloJesus.exe"

:: Compile game using PyInstaller
cd %ROOT%
py -m PyInstaller --onefile --noconsole --icon=assets/ui/icon.ico --name TechnoloJesus game_logic/main.py

:: Move build to target folder
move "%ROOT%\dist\TechnoloJesus.exe" "%BUILD_DIR%\TechnoloJesus.exe"
rmdir /s /q "%ROOT%\build"
rmdir /s /q "%ROOT%\dist"
rmdir /s /q "%ROOT%\__pycache__"

echo Build complete!
pause
