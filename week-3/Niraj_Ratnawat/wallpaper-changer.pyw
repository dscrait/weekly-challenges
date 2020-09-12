import ctypes 
import os
from datetime import datetime
import random
now = datetime.now()
today10pm = now.replace(hour = 22, minute = 0, second = 0, microsecond = 0)

def get_images():
    lis = []
    for file in os.listdir("wallpapers/"):
        if file.endswith(".jpg") or file.endswith(".png") or file.endswith(".jpeg") or file.endswith(".bmp"):
           lis.append(os.path.abspath(os.path.join("wallpapers/", file)))
    return lis

images = get_images()

w1 = random.choice(images)
print(w1)

if(today10pm<now):
    ctypes.windll.user32.SystemParametersInfoW(20, 0, w1, 0)
