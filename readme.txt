EyeRis V1.19.0
This program was built in order to add an alternative to how we approach and interact with our computers
and phones. 
-------------------------------------------------------------------------------------------------
In order for this to work properly, you need the following modules:
numpy
opencv
pynput
-------------------------------------------------------------------------------------------------
Only works with python 3.5+

-------------------------------------------------------------------------------------------------
In order to change the settings of the program, please run "configure.py", which should be in the same directory as this file. Settings are contained in 'settings.txt', and are set to their recommended values.

Sensitivity will determine how easily the program will react to movement. It's set to medium by default.
Which webcam you are using, is your webcam's number relative to your other webcams. Usually main webcam is 0, secondary one is 1. It's set to 0 by default.

You can toggle between media and scrolling mode by using 'configure.py'. It's set to media controls by default. 
-------------------------------------------------------------------------------------------------
How this program works:
For media like spotify, flick your hands towards the right side of the webcam feed to play the next song. Flick the left side to play the previous song. 

In order to pause the media, put your hand or palm up to the webcam and make sure it's covering the webcam. Also make sure you are in media mode for media controls.

You can exit the program by pressing the 'E' key while the camera feed window is opened!

For scrolling mode, it's pretty much exactly what it sounds like. It's used to scroll through books and webpages using your webcam! :)
-------------------------------------------------------------------------------------------------

PS: There's a file called 'music_bot.py' part of the files we included on our GitHub Repo.
It's a scrapped addition to our main project, a Discord Music Bot. Not relevant, but was fun to make!