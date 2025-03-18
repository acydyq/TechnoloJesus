@echo off
cd /d C:\Users\Shadow\Documents\.PROJECTS\TechnoloJesus
echo Creating project structure...

:: Create necessary directories
mkdir core
mkdir ui
mkdir data
mkdir scripts

:: Create placeholder files
echo. > core/game_loop.py
echo. > core/employees.py
echo. > ui/gui.py
echo. > data/game_data.db
echo. > main.py
echo. > requirements.txt
echo. > README.md

:: Add .gitkeep to empty folders
echo. > core/.gitkeep
echo. > ui/.gitkeep
echo. > data/.gitkeep
echo. > scripts/.gitkeep

echo Project structure created successfully!
pause
