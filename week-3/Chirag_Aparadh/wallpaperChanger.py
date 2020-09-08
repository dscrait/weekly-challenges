#!/usr/bin/env python

# this scritp automatically changes wallpaper every 10 seconds
# the scritp is bad but it works!
#also for some reason it works only with bmp images

import ctypes
import random
import os
import schedule 
import time
import sys


def get_path():
    path = os.path.abspath('wallpapers')
    for root, root1, files in os.walk('wallpapers'):
    	no_of_wallpapers = len(files)	
    random_no = random.randint(0, no_of_wallpapers-1)
    path = os.path.join(path, files[random_no])
    
       
    return path

def main():
    path = get_path()
    ctypes.windll.user32.SystemParametersInfoW(20, 0, path, 0)


schedule.every(10).seconds.do(main)

while 1:
	schedule.run_pending()
	time.sleep(1)




