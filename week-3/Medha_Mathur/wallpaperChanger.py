import struct
import ctypes
import os
from datetime import datetime

folder = os.path.dirname(os.path.abspath('wallpaper.jpg'))

image_files = []
for r, d, f in os.walk(folder):
    for file in f:
        if '.jpg' in file:
            image_files.append(os.path.join(r, file))

SPI_SETDESKWALLPAPER = 20


def is_64_windows():
    return struct.calcsize('P') * 8 == 64


def get_sys_parameters_info():
    return ctypes.windll.user32.SystemParametersInfoW if is_64_windows() \
        else ctypes.windll.user32.SystemParametersInfoA


def change_wallpaper():
    sys_parameters_info = get_sys_parameters_info()
    r = sys_parameters_info(SPI_SETDESKWALLPAPER, 0, WALLPAPER_PATH, 3)
    if not r:
        print(ctypes.WinError())

now = datetime.now()

today11am = now.replace(hour=2, minute=0, second=10, microsecond=0)
today9pm = now.replace(hour=21, minute=0, second=0, microsecond=0)

WALLPAPER_PATH=""
if __name__=="__main__":
    for i in range(len(image_files)-1):
        if now>today11am and now<today9pm:
            WALLPAPER_PATH = image_files[i]
        else:
            WALLPAPER_PATH = image_files[i+1]
    change_wallpaper()
