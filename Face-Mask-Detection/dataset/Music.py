from pygame import mixer
import time

# Starting the mixer
mixer.init()

# Loading the song
mixer.music.load("Alert\warning_alert_2011.mp3")

# Setting the volume
mixer.music.set_volume(0.7)

# Start playing the song
mixer.music.play()

# sleep
time.sleep(3)
# stop the music
mixer.music.stop()

