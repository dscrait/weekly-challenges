import ctypes 
import os
from datetime import datetime

#current time:
now = datetime.now()

# 10pm tonight
today10pm = now.replace(hour = 22, minute = 0, second = 0, microsecond = 0)

# path of wallpaper 1
w1 = os.path.abspath("wallpapers/milkyway.jpg")

# path of wallpaper 2:
w2 = os.path.abspath("wallpapers/evening.jpg")


if(today10pm>now):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, w1, 0)
else:
    ctypes.windll.user32.SystemParametersInfoW(20, 0, w2, 0)



