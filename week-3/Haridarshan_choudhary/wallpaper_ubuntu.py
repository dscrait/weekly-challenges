
import os
import time

i=1
while(True):
    output_image = "wallpapers/image"+str(i)+".jpg"
    msg = "wget -O "+ str(output_image) + " https://source.unsplash.com/450x650/?space"
    os.system(msg)
    current_directory = str(os.getcwd())
    wallpaper_string = "gsettings set org.cinnamon.desktop.background picture-uri  file://"+current_directory+"wallpapers/"+output_image
    os.system(wallpaper_string)
    time.sleep(20)
    i+=1