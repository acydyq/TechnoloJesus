@echo off
echo Setting up TechnoloJesus development environment...

REM Define project path
set PROJECT_PATH=C:\Users\Shadow\Documents\.PROJECTS\TechnoloJesus

REM Check if the project directory exists, create if necessary
if not exist "%PROJECT_PATH%" (
    echo Creating project directory...
    mkdir "%PROJECT_PATH%"
)

cd "%PROJECT_PATH%"

REM Ensure file_structure.bat is in the correct location before running
if exist "%PROJECT_PATH%\scripts\file_structure.bat" (
    call scripts\file_structure.bat
) else (
    echo ERROR: file_structure.bat not found in scripts\ folder. Manually run it or move it to the correct location.
    pause
    exit /b
)

REM Initialize Git repository if not already initialized
if not exist ".git" (
    echo Initializing Git repository in %PROJECT_PATH%...
    git init
    git branch -M main
)

REM Create virtual environment (Windows)
if not exist "venv" (
    echo Creating virtual environment...
    python -m venv venv
)

REM Activate virtual environment
call venv\Scripts\activate

REM Ensure pip is upgraded properly
echo Upgrading pip...
python -m pip install --upgrade pip

REM Install dependencies
echo Installing dependencies...
pip install pygame matplotlib pytmx

REM SQLite3 is built into Python; confirm it's accessible
python -c "import sqlite3; print('SQLite3 is installed and accessible')" || (
    echo ERROR: SQLite3 is missing or not accessible!
    pause
    exit /b
)

REM Ensure initial Git commit exists
git add .
git commit -m "Initial commit - TechnoloJesus project setup"

echo Setup complete! Run 'main.py' to start development.
pause
