@echo off
setlocal EnableDelayedExpansion

echo Current directory: %CD%

REM Check if structure.txt exists
if not exist "structure.txt" (
    echo ERROR: structure.txt not found!
    goto :end
)

echo Creating structure from structure.txt (skipping first line):
echo --------------------------------
set "skipFirst=true"
for /f "tokens=*" %%i in (structure.txt) do (
    if defined skipFirst (
        set "skipFirst="
        echo Skipping project folder: %%i
    ) else (
        set "path=%%i"
        set "path=!path:/=\!"
        echo Processing: !path!
        
        REM Check if it's a folder (no extension) or file
        if "!path:~-4!"==".txt" (
            REM File (checking for .txt extension)
            type nul > "!path!" 2>nul
            if errorlevel 1 (
                echo Failed to create file: !path!
            ) else (
                echo Created file: !path!
            )
        ) else (
            REM Folder
            mkdir "!path!" 2>nul
            if errorlevel 1 (
                echo Failed to create folder: !path!
            ) else (
                echo Created folder: !path!
            )
        )
    )
)

:end
echo Done.
pause