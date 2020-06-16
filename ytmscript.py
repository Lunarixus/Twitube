#
# Copyright (C) Lunarixus 2020
# Script to retrieve playing song from YT music
# and write it to a text file for streaming in OBS
#

# Imports
import urllib.request
from bs4 import BeautifulSoup
import time
import _thread

# Variables
port = "9863"
url = "http://localhost:%s/" % port

# Define scraping function
def scrapesong(url):
    request = urllib.request.urlopen(url)
    data = request.read()
    soup = BeautifulSoup(data, features="html.parser")
    get_song = soup.find('div').get_text()
    song = get_song.replace("""
                          """, " - ")
    song = " ".join(song.split())
    return song

# Define function for scraping and writing to file
def grabandwrite(url):
    while True:
        print("[INFO]: Scraping currently playing song...")
        song = scrapesong(url)
        if song != "":
            print("[INFO]: Current song:", scrapesong(url))
            file = open("currentplaying.txt", "r+")
            file.truncate(0)
            print("[INFO]: File cleared!")
            file.close()
            file = open("currentplaying.txt", "w+")
            file.write(song)
            print("[INFO]: Song written to file!")
            file.close()

        time.sleep(1)

# Make thread and start program
print("[INFO]: Starting thread...")
try:
    _thread.start_new_thread( grabandwrite(url), ("Thread-1", 2, ) )
except:
    print("[FAIL]: Failed to make thread!")

while 1:
    pass
