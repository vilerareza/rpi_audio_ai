'''
This program is to be run on Raspberry Pi and require the TTS library to be installed.
This program accept text to be synthesized from CLI argument and create WAV file as a result
'''

import time
import argparse
import torch
from TTS.api import TTS
from pygame import mixer


# Get device type to configure pytorch inference
device = "cuda" if torch.cuda.is_available() else "cpu"


def main(input_text:str, output_file:str = 'speech.wav', play = True, audio_vol = 0.7):

    print ('Starting...')
    
    # Initialize single speaker tts object: tacotron model - english language - ljspeech dataset 
    # The model will be downloaded at the first time
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=True).to(device)

    '''Synthesize speech and write it to wav file'''
    wav = tts.tts_to_file(input_text, file_path=output_file)


    if play:

        '''Play the generated speech'''
        mixer.init()
        # Loading the audio
        mixer.music.load(output_file)
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
    parser.add_argument('--text', type = str, required = True)
    parser.add_argument('--output_file', type = str, required = True)
    parser.add_argument('--play', action='store_true', required = False)
    parser.add_argument('--vol', type = int, default = 7, required = False)

    # Parsing
    args = parser.parse_args()
    # Input text string
    input_text = args.text
    # File path for writing output
    output_file = args.output_file
    # Play synthesized sound
    play = True
    if not (args.play):
        play = False
    audio_vol = (args.vol)/10

    # Run
    main(input_text=input_text, 
         output_file=output_file,
         play = play,
         audio_vol=audio_vol
         )