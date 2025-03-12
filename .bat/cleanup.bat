@echo off
echo Cleaning up temporary files...

:: Define root directory
set ROOT=C:\Users\Shadow\Documents\.PROJECTS\TechnoloJesus

:: Remove PyInstaller temporary files
rmdir /s /q "%ROOT%\build"
rmdir /s /q "%ROOT%\dist"
rmdir /s /q "%ROOT%\__pycache__"
del "%ROOT%\TechnoloJesus.spec"

echo Cleanup complete!
pause
