@echo off
cd /d C:\Users\Shadow\Documents\.PROJECTS\TechnoloJesus
echo Initializing Git repository...
git init
git remote add origin https://github.com/YOUR_GITHUB_USERNAME/TechnoloJesus.git
git add .
git commit -m "Initial commit - TechnoloJesus Project Setup"
git branch -M main
git push -u origin main
echo GitHub repository initialized and first push complete!
pause
