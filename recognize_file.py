'''
Transcribe audio from file
Test audio file path is 'audio/sample/up1.wav'
'''

import argparse
from recognizer import SpeechRecognizer
 

def main(path_audio_file, model_dir):
    
    try:

        speech_recognizer = SpeechRecognizer(model_dir)
        audio_text = speech_recognizer.transcribe_from_file(path_audio_file)
        print(f"Transcription result: {audio_text.split(' ')}")
             
    except Exception as e:
        print(f'Failed to transcribe {e}')
         

if __name__ == '__main__':

    # Argument handler
    parser = argparse.ArgumentParser()
    parser.add_argument('--audio_file', type = str, required = True)
    parser.add_argument('--model_dir', type = str, default='models/', required = False)

    # Parsing
    args = parser.parse_args()
    # Path to audio file
    path_audio_file = args.audio_file
    # Directory of saved model
    model_dir = args.model_dir

    # Run
    main(path_audio_file=path_audio_file, 
         model_dir=model_dir
         )