# Python wallpaper automation challenge

**Ussage**
- Store your wallpapers under wallpaper folder
- the program will randomly choose an image from the folder to be set as a wallpaper
- if there's only one image it'll set that image as wallpaper
Run ```python changeWallpaper.py```
or run the script.bat file


**Instructions to schedule change wallpaper task**
- open 'Task Scheduler' in windows ``` control panel> system and security> administrative tools> Task Scheduler```
- click on ```Create a basic task``` 
- Enter name and description of your choice
- Under triggers set the time when you want to change wallpaper
- Under action select start a program then browse and select ```script.bat``` file
- click ok
- Done

Your wallpaper will change during the scheduled time