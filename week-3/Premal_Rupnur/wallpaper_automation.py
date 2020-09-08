import ctypes
import os
from datetime import datetime
import random



#Adding all image paths from folder into a list.
def get_images():
    image_files = []

    path = os.path.join(os.getcwd(),'wallpapers')
    with os.scandir(path) as f:
        for file in f:
            if '.jpg' in file.name:
                image_files.append(os.path.join(os.getcwd(),file))
    return image_files

SPI_SETDESKWALLPAPER = 20

#Returns correct version of SystemParametersInfo function.
def get_sys_parameters_info():
    return ctypes.windll.user32.SystemParametersInfoW 
       
#function to initiate wallpaper change 
def change_wallpaper():
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)
    if not r:
        print(ctypes.WinError())

#Getting current time.        
now = datetime.now()

#Setting time to 10am for wallpaper changing.
today10am = now.replace(hour=10, minute=0, second=0, microsecond=0)

# At 10am   wallpaper are changed.
WALLPAPER_PATH=""
if __name__=="__main__":
    
    image_files = get_images()
    random.shuffle(image_files)
    if(today10am==now):
        WALLPAPER_PATH = image_files[1]
    
    change_wallpaper()