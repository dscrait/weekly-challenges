import ctypes 
from datetime import datetime
now = datetime.now()
today10pm = now.replace(hour = 22, minute = 0, second = 0, microsecond = 0)

#Justify the absolute path of your wallpaper images 
#Absolute path of wallpaper 1: 
w1 = r"C:\Users\Niraj\weekly-challenges\week-3\Niraj_Ratnawat\wallpapers\milkyway.jpg"

#Absolute path of wallpaper 2:
w2 = r"C:\Users\Niraj\weekly-challenges\week-3\Niraj_Ratnawat\wallpapers\evening.jpg"

if(today10pm>now):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, w1, 0)
else:
    ctypes.windll.user32.SystemParametersInfoW(20, 0, w2, 0)



