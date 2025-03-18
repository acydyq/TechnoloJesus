@echo off
cd /d C:\Users\Shadow\Documents\.PROJECTS\TechnoloJesus
echo Staging all changes...
git add .
set /p commit_msg="Enter commit message: "
git commit -m "%commit_msg%"
git push origin main
echo Update pushed to GitHub!
pause
