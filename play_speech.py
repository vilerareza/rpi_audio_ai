'''
Program to test the basic audio function using Pygame.
The speaker should be connected to 3.5 mm stereo jack on the RPi
'''

import argparse
import time
from pygame import mixer


def main(audio_path, audio_vol):

    # Initialize pygame mixer
    mixer.init()
    # Loading the audio
    mixer.music.load(audio_path)
    # Setting the volume
    mixer.music.set_volume(audio_vol)
    # Play the audio file

    print ('Connect speaker device to 3.5mm stereo audio jack at the RPi')

    while True:
        mixer.music.play()
        query = input("Press 'r' to play again or 'q' to quit: ")
        if query == 'q':
            break
        time.sleep(1)


if __name__ == '__main__':

    # Argument handler
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type = str, required = True)
    parser.add_argument('--vols', type = int, default=1, required = False)
    

    # Parsing
    args = parser.parse_args()
    # Path to audio_file
    audio_path = args.input_file
    # Audio volume
    audio_vol = args.vols

    # Run
    main(audio_path=audio_path, 
         audio_vol=audio_vol,
         )