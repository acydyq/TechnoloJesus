@echo off
echo Launching TechnoloJesus...

:: Define root directory
set ROOT=C:\Users\Shadow\Documents\.PROJECTS\TechnoloJesus
set LOGFILE=%ROOT%\build\logs\game_log.txt

:: Run the game and save logs
cd %ROOT%
py game_logic/main.py > "%LOGFILE%" 2>&1

echo Game closed. Check logs for details.
pause
