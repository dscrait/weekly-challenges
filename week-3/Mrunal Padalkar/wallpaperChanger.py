import struct
import ctypes
import os
from datetime import datetime

#Getting folder path in which images are stored.
folder = os.path.dirname(os.path.abspath('wallpaper.jpg'))

#Adding all image paths from folder into a list.
image_files = []
for r, d, f in os.walk(folder):
    for file in f:
        if '.jpg' in file:
            image_files.append(os.path.join(r, file))

SPI_SETDESKWALLPAPER = 20

#Find out how many bits is OS.
def is_64_windows():
    return struct.calcsize('P') * 8 == 64

#Based on if this is 32bit or 64bit returns correct version of SystemParametersInfo function.
def get_sys_parameters_info():
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA


def change_wallpaper():
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)
    # When the SPI_SETDESKWALLPAPER flag is used,
    # SystemParametersInfo returns TRUE
    # unless there is an error (like when the specified file doesn't exist).
    if not r:
        print(ctypes.WinError())

#Getting current time.
now = datetime.now()

#Setting time variables for wallpaper changing.
today10am = now.replace(hour=10, minute=0, second=0, microsecond=0)
today9pm = now.replace(hour=21, minute=0, second=0, microsecond=0)

# Based on time limit, wallpaper are changed.
WALLPAPER_PATH=""
if __name__=="__main__":
    #Traversing the list of image paths.
    for i in range(len(image_files)-1):
        #Between 11 AM and 9 PM, the ith image will be made wallpaper.
        if now>today10am and now<today9pm:
            WALLPAPER_PATH = image_files[i]
        #After 9 PM or before 11 AM, the (i+1)th iamge is made wallpaper.
        else:
            WALLPAPER_PATH = image_files[i+1]
    change_wallpaper()
