import os
import ctypes
import time

def getFullPathOfImage(imageFilename):
	return os.path.dirname(os.path.realpath("wallpapers/" + imageFilename)) + "\\" + imageFilename

def setImage(imageFilename):
	ctypes.windll.user32.SystemParametersInfoW(20, 0, getFullPathOfImage(imageFilename) , 0)

choice = 1

while choice == 1:
    imgname=input('Enter the image file name you want to change the background to: ')
    time.sleep(3)
    setImage(imgname)
    print('The desktop image will change to the default choice in 5secs')
    time.sleep(5)
    setImage('w4.png')
    choice = int(input('Do you want to change the background again?(0-no/1-yes): '))