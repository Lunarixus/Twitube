# Twitube for OBS

This is a simple script I wrote which will scrape the current playing  
song from the Electron YouTube Music application for Windows, Mac and Linux.  

# How to use
1. Install the required modules with ```pip3 install -r requirements.txt```
2. Download the Electron YouTube Music app from [here](https://ytmdesktop.app/).
3. Log in and select the gear icon ⚙️.
4. Under "Integration" enable the companion server.
5. Run the script and check the outputted currentplaying.txt contains your song.
6. Open OBS and add a text source
7. In the text source window tick the "from file" checkbox and select the currentplaying.txt file.
8. Profit.

# Credits
Lunarixus - Original script developer.  
YTMDesktopApp - Creating this awesome YouTube Music client.
