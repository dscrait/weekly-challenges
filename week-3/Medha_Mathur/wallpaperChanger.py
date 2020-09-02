import struct
import ctypes


SPI_SETDESKWALLPAPER = 20
WALLPAPER_PATH = 'C:\\Users\LENOVO\Desktop\weekly-challenges\week-3\Medha_Mathur\wallpaper.jpg'


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


change_wallpaper()
