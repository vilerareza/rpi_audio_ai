import argparse
from recognizer import SpeechRecognizer
import speech_recognition as sr
import time
from pygame import mixer


def main(model_dir):
        
    try:

        # Initialize speech recognizer
        speech_recognizer = SpeechRecognizer(model_dir)
        # Initialize sound recognizer module
        r = sr.Recognizer()

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
                audio_text = speech_recognizer.transcribe(audio_data)
                audio_text = audio_text.split(' ')
                print(f"Transcription result: {audio_text}")
                
                # String cleaning
                audio_text = [word.lower() for word in audio_text]
                audio_text = [word.replace(',', '') for word in audio_text]
                audio_text = [word.replace ('.', '') for word in audio_text]
                audio_text = [word.strip() for word in audio_text]

                print (audio_text)

                if any(word in ['hello', 'hi', 'hey', 'halo'] for word in audio_text):
                    print ('PLAY')
                    # Initialize pygame mixer
                    mixer.init()
                    # Loading the audio
                    mixer.music.load('audio/library/my_name.wav')
                    # Setting the volume
                    mixer.music.set_volume(10)
                    # Play the audio file
                    mixer.music.play()

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