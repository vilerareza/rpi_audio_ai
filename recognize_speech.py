import argparse
from recognizer import SpeechRecognizer
import speech_recognition as sr
import time
from pygame import mixer
import subprocess

from conversation_lookup import conversation


def main(model_dir):
        
    try:

        # Initialize speech recognizer
        speech_recognizer = SpeechRecognizer(model_dir)
        # Initialize sound recognizer module
        r = sr.Recognizer()
        # Initialize mixer object for playing response audio file
        mixer.init()

        while True:   

            # use the microphone as source for input.
            with sr.Microphone(sample_rate=16000) as source_:
                
                # Adjusting for noise
                r.adjust_for_ambient_noise(source_, duration=0.2)

                #listens for the user's input
                print ('listening...')
                audio_data = r.listen(source_)
                #print (f'sr: {audio_data.sample_rate}, width: {audio_data.sample_width}')
                # Get audio raw data
                audio_data = audio_data.get_raw_data()
                # Transcribe
                print ('transcribing')
                words = speech_recognizer.transcribe(audio_data)
                words = words.split(' ')
                print(f"Transcription result: {words}")
                
                # String cleaning
                words = [word.lower() for word in words]
                words = [word.replace(',', '') for word in words]
                words = [word.replace ('.', '') for word in words]
                words = [word.replace ('?', '') for word in words]
                words = [word.replace ('!', '') for word in words]
                words = [word.strip() for word in words]

                print (words)

                '''Conversation response'''
                # Looking up response audio file
                response_audio = conversation(words)
                if response_audio:
                    result = subprocess.run(['aplay','--format=S16_LE', '--rate=16000', response_audio])
                    # # Loading the audio
                    # mixer.music.load(response_audio)
                    # # Setting the volume
                    # mixer.music.set_volume(10)
                    # # Play the audio file
                    # mixer.music.play()

                time.sleep(0.5)
             
    except Exception as e:
        print(f'Failed to transcribe {e}')


if __name__ == '__main__':

    # Argument handler
    parser = argparse.ArgumentParser()
    parser.add_argument('--model_dir', type = str, default='models/', required = False)

    # Parsing
    args = parser.parse_args()
    # Directory of saved model
    model_dir = args.model_dir

    # Run
    main(model_dir=model_dir)