# تثبيت المكتبات اللازمة
# pip install torch transformers datasets soundfile librosa

import torch
import librosa
import numpy as np
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor

# Download the model and the processor
processor = Wav2Vec2Processor.from_pretrained("jonatasgrosman/wav2vec2-large-xlsr-53-arabic")
model = Wav2Vec2ForCTC.from_pretrained("jonatasgrosman/wav2vec2-large-xlsr-53-arabic")

# function to load an audio file and process it
def load_audio(file_path):
    # Load the audio file using librosa (sample rate of 16 kHz).
    audio, rate = librosa.load(file_path, sr=16000)
    return audio

# A function for Arabic speech recognition from an audio file.
def recognize_arabic_speech(file_path):
    # Load and process the audio file.
    audio = load_audio(file_path)
    
    # Convert audio data into a PyTorch tensor.
    inputs = processor(audio, sampling_rate=16000, return_tensors="pt", padding=True)
    
    # Get the model's predictions.
    with torch.no_grad():
        logits = model(inputs.input_values).logits
    
    # Extract the highest probability for characters.
    predicted_ids = torch.argmax(logits, dim=-1)
    
    # Convert prediction IDs to text.
    transcription = processor.batch_decode(predicted_ids)
    
    return transcription[0]

# Example
if __name__ == "__main__":
    audio_file_path = "C:/Users/3ab3zeez/Downloads/Are there Persian words in the Qur'an.mp3"
    
    try:
        result = recognize_arabic_speech(audio_file_path)
        print("النص المُستخرج من الصوت:")
        print(result)
    except Exception as e:
        print(f"حدث خطأ: {e}")

# ----------------------------------------------------
# An advanced example for handling a collection of audio files.
# ----------------------------------------------------

def batch_recognize_arabic(audio_files):
    results = {}
    
    for file_path in audio_files:
        try:
            transcript = recognize_arabic_speech(file_path)
            results[file_path] = transcript
        except Exception as e:
            results[file_path] = f"خطأ: {str(e)}"
    
    return results

# An example of using parallel processing to speed up the task.
def parallel_recognize_arabic(audio_files, num_workers=4):
    from concurrent.futures import ThreadPoolExecutor
    
    results = {}
    
    def process_file(file_path):
        try:
            return file_path, recognize_arabic_speech(file_path)
        except Exception as e:
            return file_path, f"خطأ: {str(e)}"
    
    with ThreadPoolExecutor(max_workers=num_workers) as executor:
        for file_path, transcript in executor.map(process_file, audio_files):
            results[file_path] = transcript
    
    return results