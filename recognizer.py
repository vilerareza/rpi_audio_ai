from transformers import WhisperProcessor, WhisperForConditionalGeneration
import torch
import torchaudio
import numpy as np
import time
 

class SpeechRecognizer:

    def __init__(self, model_dir) -> None:
        # Path to the saved Whisper model and processor
        self.model_dir = model_dir
        # Getting device configuration and whisper model name
        self.device = "cuda:0" if torch.cuda.is_available() else "cpu"
        # Load whisper model from file
        print ('Loading Whisper model...')
        self.whisper_processor = WhisperProcessor.from_pretrained(self.model_dir)
        self.whisper_model = WhisperForConditionalGeneration.from_pretrained(self.model_dir).to(self.device)
        self.forced_decoder_ids = self.whisper_processor.get_decoder_prompt_ids(language='english', task='transcribe')
        # Excercise the whisper processor at init so that next inference is faster
        dummy_features = self.whisper_processor(torch.tensor([0]), return_tensors="pt", sampling_rate=16000).input_features.to(self.device)
        dummy_ids = self.whisper_model.generate(dummy_features, forced_decoder_ids=self.forced_decoder_ids)
        print ('Whisper model loaded')


    def preprocess(self, data):
        # Convert data from int16 to float32 or float16 using 32768 division.
        # Ref: https://github.com/openai/whisper/discussions/908
        audio_data = torch.from_numpy(np.frombuffer(data, np.int16).flatten().astype(np.float32) / 32768.0)
        resampler = torchaudio.transforms.Resample(16000, 16000)
        audio_data = resampler(audio_data)
        return audio_data.squeeze()


    def load_audio(self, audio_path):
        """Load the audio file & convert to 16,000 sampling rate"""
        # load our wav file
        speech, sr = torchaudio.load(audio_path)
        resampler = torchaudio.transforms.Resample(sr, 16000)
        speech = resampler(speech)
        return speech.squeeze()


    def transcribe(self, audio_data, skip_special_tokens=True):
        audio_tensor = self.preprocess(audio_data)
        # get the input features from the audio file
        input_features = self.whisper_processor(audio_tensor, return_tensors="pt", sampling_rate=16000).input_features.to(self.device)
        # generate the transcription
        predicted_ids = self.whisper_model.generate(input_features, forced_decoder_ids=self.forced_decoder_ids)
        # decode the predicted ids
        transcription = self.whisper_processor.batch_decode(predicted_ids, skip_special_tokens=skip_special_tokens)[0]
        return transcription
    

    def transcribe_from_file(self, file_path, language="english", skip_special_tokens=True):
        audio_tensor = self.load_audio(file_path)
        # get the input features from the audio file
        input_features = self.whisper_processor(audio_tensor, return_tensors="pt", sampling_rate=16000).input_features.to(self.device)
        # get the forced decoder ids
        forced_decoder_ids = self.whisper_processor.get_decoder_prompt_ids(language=language, task="transcribe")
        # generate the transcription
        predicted_ids = self.whisper_model.generate(input_features, forced_decoder_ids=forced_decoder_ids)
        # decode the predicted ids
        transcription = self.whisper_processor.batch_decode(predicted_ids, skip_special_tokens=skip_special_tokens)[0]
        return transcription