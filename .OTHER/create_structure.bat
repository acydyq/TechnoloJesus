@echo off
setlocal enabledelayedexpansion

echo Creating project structure...

:: List of folders to create
set "folders=core ui data scripts"

:: List of files to create
set "files=core/game_loop.py ui/gui.py data/game_data.db scripts/setup.bat scripts/build.bat main.py requirements.txt README.md"

:: Create folders
for %%F in (%folders%) do (
    if not exist "%%F" (
        mkdir "%%F"
        echo Created folder: %%F
    )
    if not exist "%%F\.gitkeep" (
        echo. > "%%F\.gitkeep"
        echo Added .gitkeep to: %%F
    )
)

:: Create files
for %%F in (%files%) do (
    if not exist "%%F" (
        echo. > "%%F"
        echo Created file: %%F
    )
)

echo Project setup complete!
pause
