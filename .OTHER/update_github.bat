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

REM Create project folder structure (if not already created)
call ..\file_structure.bat

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

REM Install dependencies
echo Installing dependencies...
pip install --upgrade pip
pip install pygame matplotlib sqlite3 pytmx

REM Ensure initial Git commit exists
echo Committing initial project files...
git add .
git commit -m "Initial commit - TechnoloJesus project setup"

echo Setup complete! Run 'main.py' to start development.
pause
