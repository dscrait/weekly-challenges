import os
import ctypes
from datetime import datetime
import random

#Add all the wallpapers from the directory in a list
def get_images():
    pref_extensions = ['jpg', 'png',  'jpeg']
    with os.scandir("./wallpapers") as files:
        images = []
        for image in files:
            if image.is_file and image.name.split('.')[1] in pref_extensions:
                images.append(os.path.join(os.getcwd(),'wallpapers\\'+str(image.name)))
    return images


SPI_SETDESKWALLPAPER = 20 

# # Returns correct version of SystemParametersInfo function.
def get_sys_parameters_info():
    return ctypes.windll.user32.SystemParametersInfoW 

# # Method to change the wallpaper
def change_wallpaper():
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)
    if not r:
        print(ctypes.WinError())

# # Get current time
now = datetime.now()

# # Set time for wallpaper changing
today9pm = now.replace(hour=21, minute=0, second=0, microsecond=0)

# # #At 6am the wallpaper changes
WALLPAPER_PATH=""
if __name__=="__main__":

    image_files = get_images()
    random.shuffle(image_files)
    if(today9pm==now):
        WALLPAPER_PATH = image_files[1]

        change_wallpaper() 