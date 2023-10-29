'''
Contain helper function for conversation response lookup
'''

import os

# Path to audio files library
audio_library_path = 'audio/library/'

# Dictionary that defines pairs of recognized words and response audio file
response_file_dict = {
    'greeting_1': os.path.join(audio_library_path, 'my_name.wav'),
    'greeting_2': os.path.join(audio_library_path, 'how_are_you.wav'),
    'greeting_3': os.path.join(audio_library_path, 'good_morning.wav'),
    'greeting_4': os.path.join(audio_library_path, 'good_afternoon.wav'),
    'greeting_5': os.path.join(audio_library_path, 'good_evening.wav')
}

# Conversation lookup function that returns response  audio file name
def conversation(words, response_file_dict=response_file_dict):
    
    # Greeting 1
    if any(word in ['hello', 'hi', 'hey', 'halo'] for word in words):
        return response_file_dict['greeting_1']
    
    # Greeting 2
    if all(word in ['how', 'are', 'you'] for word in words):
        return response_file_dict['greeting_2']
    
    # Greeting 3
    if all(word in ['good', 'morning'] for word in words):
        return response_file_dict['greeting_3']
    
    # Greeting 4
    if all(word in ['good', 'afternoon'] for word in words):
        return response_file_dict['greeting_4']
    
    # Greeting 5
    if all(word in ['good', 'evening'] for word in words):
        return response_file_dict['greeting_5']
    
    return None
