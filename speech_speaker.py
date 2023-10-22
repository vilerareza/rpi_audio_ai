import time
from pygame import mixer
 

class SpeechSpeaker:

    def __init__(self) -> None:
        # Initialize pygame mixer
        self.mixer = mixer.init()

    def load_and_play(self, audio_path, audio_vol=7):  
        # Load and play the audio file
        try:      
            print ('Connect speaker device to 3.5mm stereo audio jack at the RPi')
            # Loading the audio
            self.mixer.music.load(audio_path)
            # Setting the volume
            self.mixer.music.set_volume(audio_vol)
            # Play the audio file
            self.mixer.music.play()
    
        except Exception as e:
            print (f'Failed to play {audio_path}')


    def load(self, audio_path):  
        # Loading the audio
        try:      
            self.mixer.music.load(audio_path)    
        except Exception as e:
            print (f'Failed to load {audio_path}')


    def play(self, audio_vol=7):
        # Play the loaded audio
        try:
            # Setting the volume
            self.mixer.music.set_volume(audio_vol)
            # Play the audio
            self.mixer.music.play()
            time.sleep(1)
        except Exception as e:
            print(f'Failed to play. No file is loaded')