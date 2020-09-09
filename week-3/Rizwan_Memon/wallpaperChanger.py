import os
import requests
import datetime
import wget
from dotenv import load_dotenv
import shutil


def downloadWallpaper():
  # Unsplash API
  URL = 'https://api.unsplash.com/photos/random?client_id=' + os.environ.get('ACCESS_KEY')

  # Parameters
  params = {
		'query': 'HD wallpapers',
		'orientation': 'landscape'
	}

  response = requests.get(URL, params=params).json()

  image_source = response['urls']['full']

  image = wget.download(image_source, '/tmp/wallpaper.jpg')
  return image

def saveToCollection():
  # Source path  
  source = '/tmp/wallpaper.jpg'
    
  # Destination path  
  destination = os.getenv("HOME") +'/.wallpaper/wallpaper.jpg'

  # Move the File to .wallpaper Directory
  shutil.move(source, destination)

def setWallpaper():
  currentHour = datetime.datetime.now().hour
  if 18 < currentHour < 21:
    os.system("feh --bg-fill --randomize ~/.wallpaper/*")  
  
load_dotenv()
downloadWallpaper()
setWallpaper()
# saveToCollection()