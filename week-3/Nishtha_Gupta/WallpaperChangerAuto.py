import ctypes
import os
import random
import time


def getFullPathOfImage(imageFilename):
	return os.path.dirname(os.path.realpath( "wallpapers/" + imageFilename)) + "\\" + imageFilename

def setImage(imageFilename):
	ctypes.windll.user32.SystemParametersInfoW(20, 0, getFullPathOfImage(imageFilename) , 0)

choice = 1

while choice <= 5:
    n = random.randint(1, 11)
    imgname = 'w' + str(n) + '.jpg'
    if n == 4:
        imgname = 'w' + str(n) + '.png'
    setImage(imgname)
    print('The desktop image will change to the default choice in 5secs')
    time.sleep(6)
    setImage('w4.png')
    choice += 1
    print("The changing will stop after", 5 - choice + 1, 'more times')