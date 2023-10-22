'''
Program to test the basic audio function using Pygame.
The speaker should be connected to 3.5 mm stereo jack on the RPi
'''

import argparse
import time
from pygame import mixer

from speech_speaker import SpeechSpeaker


def main(audio_path, audio_vol):
    
    print ('Connect speaker device to 3.5mm stereo audio jack at the RPi')
    
    # Initialize speech speaker object
    speech_speaker = SpeechSpeaker()
    # Load the audio file to the speech speaker
    speech_speaker.load(audio_path=audio_path)
    while True:
        speech_speaker.play(audio_vol=audio_vol)
        query = input("Press 'r' to play again or 'q' to quit: ")
        if query == 'q':
            break
        time.sleep(1)


if __name__ == '__main__':

    # Argument handler
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type = str, required = True)
    parser.add_argument('--vol', type = int, default=7, required = False)
    
    # Parsing
    args = parser.parse_args()
    # Path to audio_file
    audio_path = args.input_file
    # Audio volume
    audio_vol = (args.vol)/10

    # Run
    main(audio_path=audio_path, 
         audio_vol=audio_vol,
         )