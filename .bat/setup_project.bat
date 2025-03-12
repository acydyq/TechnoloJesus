@echo off
echo Setting up TechnoloJesus project structure...

:: Define root directory
set ROOT=C:\Users\Shadow\Documents\.PROJECTS\TechnoloJesus

:: Create main folders
mkdir "%ROOT%\game_logic"
mkdir "%ROOT%\assets"
mkdir "%ROOT%\assets\sprites"
mkdir "%ROOT%\assets\sounds"
mkdir "%ROOT%\assets\fonts"
mkdir "%ROOT%\assets\ui"
mkdir "%ROOT%\assets\maps"
mkdir "%ROOT%\utils"
mkdir "%ROOT%\tests"
mkdir "%ROOT%\docs"
mkdir "%ROOT%\config"
mkdir "%ROOT%\build"
mkdir "%ROOT%\build\logs"
mkdir "%ROOT%\scripts"

:: Create placeholder files
echo # Main Game Loop > "%ROOT%\game_logic\main.py"
echo "# Financial & Revenue Systems" > "%ROOT%\game_logic\economy.py"
echo "# Employee Management" > "%ROOT%\game_logic\employees.py"
echo "# Project Development" > "%ROOT%\game_logic\projects.py"
echo "# Skill Tree Mechanics" > "%ROOT%\game_logic\skill_tree.py"
echo "# Office Upgrades" > "%ROOT%\game_logic\upgrades.py"

echo "# Common Helper Functions" > "%ROOT%\utils\helpers.py"
echo "# Save/Load System" > "%ROOT%\utils\save_load.py"
echo "# AI Tools" > "%ROOT%\utils\ai_tools.py"
echo "# Blockchain Mechanics" > "%ROOT%\utils\blockchain.py"

echo "# Test Cases for Economy" > "%ROOT%\tests\test_economy.py"
echo "# Test Cases for Employees" > "%ROOT%\tests\test_employees.py"
echo "# Test Cases for Projects" > "%ROOT%\tests\test_projects.py"
echo "# Test Cases for Skill Tree" > "%ROOT%\tests\test_skills.py"

echo "# Game Design Notes" > "%ROOT%\docs\design_notes.txt"
echo "# Mechanics Overview" > "%ROOT%\docs\mechanics.txt"
echo "# Development Roadmap" > "%ROOT%\docs\roadmap.txt"

echo {} > "%ROOT%\config\settings.json"
echo {} > "%ROOT%\config\keybinds.json"

:: Initialize Git repository (if needed)
cd %ROOT%
git init

echo Project setup completed!
pause
