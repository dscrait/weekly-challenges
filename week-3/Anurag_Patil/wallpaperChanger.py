import os
from typing import List
import datetime
import random

# Get all the images from the wallpapers folder
def get_image_paths() -> List[str]:
    paths = []
    ext_list = ['png', 'jpeg', 'jpg']
    for root, _, files in os.walk('wallpapers'):
        for file in files:
            if list(filter(file.endswith, ext_list)) != []:
                paths.append(os.path.join(root, file))

    return paths

# Check if the wallpaper is same as the one applied
def same_wallpaper(wallpaper: str) -> bool:
    try: # try if the logging file exist or not
        with open('wallpaper_change.log', 'r') as f:
            lines = f.read().splitlines()
            # if file is empty
            if lines == []: 
                return False
            last_line = lines[-1]
            current_wallpaper = last_line.split(' ')[-1]
            return wallpaper == current_wallpaper
    except FileNotFoundError: # if not then make the file
        file = open('wallpaper_change.log', 'w+')
        file.close()
        return False

# Log whenever the wallpaper is applied
def log_changes(wallpaper: str):
    with open('wallpaper_change.log', 'a+') as f:
        f.write(f'{str(datetime.datetime.now())} {wallpaper}' + '\n')

# use the shell to change the wallpaper using nitrogen
def change_wallpaper(wallpaper: str):
    os.system(f'nitrogen {wallpaper} --set-zoom-fill')
    log_changes(wallpaper)


def main():
    images = get_image_paths()
    random.shuffle(images)
    new_wallpaper = images[-1] # random image everytime

    # recurse if same wallpaper
    if same_wallpaper(new_wallpaper):
        main()
    else:
        change_wallpaper(new_wallpaper)


main()
