@echo off
echo Initializing Git repository for TechnoloJesus...

:: Navigate to the project directory
cd /d "C:\Users\Shadow\Documents\.PROJECTS\TechnoloJesus"

:: Initialize git repository
git init

:: Add all files to staging
git add .

:: Create initial commit
git commit -m "Initial commit of TechnoloJesus project"

:: Create GitHub repository and link it
gh repo create TechnoloJesus --public --source=. --remote=origin

:: Push to GitHub
git push -u origin main

echo Repository creation complete!
echo You can now access your repository at: https://github.com/your-username/TechnoloJesus
pause