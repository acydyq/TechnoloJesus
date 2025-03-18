@echo off
echo Initializing Git repository for TechnoloJesus...

:: Navigate to the project directory
cd /d "C:\Users\Shadow\Documents\.PROJECTS\TechnoloJesus"

:: Since it says "Reinitialized", we'll just use the existing repo
:: No need for git init since it already exists

:: Add all files to staging
git add .

:: Create commit with changes
git commit -m "Initial commit of TechnoloJesus project"

:: Remove any existing origin remote to avoid conflicts
git remote remove origin 2>nul

:: Add the correct remote repository
git remote add origin https://github.com/acydyq/TechnoloJesus.git

:: Push to GitHub
git push -u origin main

echo Repository creation complete!
echo You can now access your repository at: https://github.com/acydyq/TechnoloJesus
pause