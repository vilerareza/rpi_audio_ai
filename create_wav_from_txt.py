import os
import argparse
import torch
from TTS.api import TTS


def main(in_file, out_dir):

    with open(in_file) as f:
        words = f.readlines()

    # Get device type to configure pytorch inference
    device = "cuda" if torch.cuda.is_available() else "cpu"

    # Initialize single speaker tts object: tacotron model - english language - ljspeech dataset 
    # The model will be downloaded at the first time
    tts = TTS(model_name="tts_models/en/ljspeech/tacotron2-DDC", progress_bar=True).to(device)

    for word in words:
        # Prepare the file name for audio file
        file_name = os.path.join(out_dir, f'{word}.wav')
        # Generate the audio file
        '''Synthesize speech and write it to wav file'''
        wav = tts.tts_to_file(word, file_path=file_name)


if __name__ == '__main__':

    # Argument handler
    parser = argparse.ArgumentParser()
    parser.add_argument('--input_file', type = str, required = True)
    parser.add_argument('--output_dir', type = str, default='audio/library/', required = False)
    

    # Parsing
    args = parser.parse_args()
    # Path to input txt file
    in_file = args.input_file
    # Directory for writing output files
    out_dir = args.output_dir

    # Run
    main(in_file=in_file, 
         out_dir=out_dir,
         )