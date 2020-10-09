import os
import ctypes
from datetime import datetime
import random

#Adding all the wallpaper images from the directory in a list
def get_images():
    pref_extensions = ['jpg', 'png',  'jpeg']
    with os.scandir("./wallpapers") as files:
        images = []
        for image in files:
            if image.is_file and image.name.split('.')[1] in pref_extensions:
                images.append(os.path.join(os.getcwd(),'wallpapers\\'+str(image.name)))
    return images


SPI_SETDESKWALLPAPER = 20 

# # #Returns correct version of SystemParametersInfo function.
def get_sys_parameters_info():
    return ctypes.windll.user32.SystemParametersInfoW 

# # #Function that changes the wallpaper
def change_wallpaper():
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)
    if not r:
        print(ctypes.WinError())

# # #Function that gets current time
now = datetime.now()

# # #Setting time for wallpaper changing
today6am = now.replace(hour=6, minute=0, second=0, microsecond=0)

# # #At 6am the wallpaper changes
WALLPAPER_PATH=""
if __name__=="__main__":
    
    image_files = get_images()
    random.shuffle(image_files)
    if(today6am==now):
        WALLPAPER_PATH = image_files[1]
    
    change_wallpaper()