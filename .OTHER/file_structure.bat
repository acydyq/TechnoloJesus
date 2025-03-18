@echo off
echo Setting up TechnoloJesus project structure...

REM Create main project directory
mkdir TechnoloJesus
cd TechnoloJesus

REM Create core directories
mkdir game_logic
mkdir assets
mkdir assets\sprites
mkdir assets\sounds
mkdir assets\fonts
mkdir assets\maps
mkdir utils
mkdir tests
mkdir docs
mkdir config
mkdir build
mkdir scripts
mkdir database

REM Create core Python files
echo. > game_logic\main.py
echo. > game_logic\startup_simulation.py
echo. > game_logic\employee_management.py
echo. > game_logic\financials.py
echo. > game_logic\shady_business.py
echo. > game_logic\ai_competitors.py
echo. > game_logic\negotiation.py
echo. > game_logic\project_management.py
echo. > game_logic\user_data_sales.py
echo. > game_logic\reports.py

REM Create utility scripts
echo. > utils\database.py
echo. > utils\dice_roll.py
echo. > utils\ui_render.py

REM Create test files
echo. > tests\test_financials.py
echo. > tests\test_employees.py
echo. > tests\test_negotiation.py

REM Create documentation files
echo. > docs\roadmap.txt
echo. > docs\design_notes.txt
echo. > docs\mechanics.txt
echo. > docs\file_structure.txt

REM Create config files
echo. > config\settings.ini
echo. > config\commands.txt

REM Create database file
echo. > database\game_data.db

REM Create automation scripts
echo. > scripts\setup_project.bat
echo. > scripts\update_github.bat

REM Create essential project files
echo. > .gitignore
echo. > README.md

echo Project structure setup complete!
pause
