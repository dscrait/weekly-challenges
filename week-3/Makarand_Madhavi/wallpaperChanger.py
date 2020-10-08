import ctypes
import os
import struct
import random

def wallpapercahange_api():
    """Check for 64 bit or 32 bit Windows OS"""
    if struct.calcsize('P') * 8 == 64:
        return ctypes.windll.user32.SystemParametersInfoW
    else:
        return ctypes.windll.user32.SystemParametersInfoA


def change():
    DIR = os.getcwd()
    SPI_SETDESKWALLPAPER = 20
    #getting images from wallpapers folder
    images = [i for i in os.listdir("wallpapers") if i.lower().endswith(('.png', '.jpg', '.jpeg','.bmp'))]

    #creating/opening log file
    try:
        f = open("wallpaper.log","r+")
    except Exception:
        f = open("wallpaper.log","w+")
    
    #select random image
    selected = random.choice(images)
    current = f.read()
    print("current= "+current)
    while(selected ==current and len(images)!=1):
        selected = random.choice(images)
    f.seek(0)
    f.write(selected)
    f.truncate()
    f.close()
    print("selected= "+selected)
    imagepath = DIR+"\\wallpapers\\"+selected

    #changing wallpaper
    api = wallpapercahange_api()
    api(SPI_SETDESKWALLPAPER, 0, imagepath, 3)

change()