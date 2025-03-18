from moviepy import VideoFileClip
from transformers import Wav2Vec2ForCTC, Wav2Vec2Processor
import os
import torch
import librosa


def convert_to_mp3(video_path: str) -> str:
    file_name = os.path.basename(video_path)[:-4]
    audio_path = f"audio_cache/{file_name}.mp3"

    audio_clip = VideoFileClip(video_path).audio
    audio_clip.write_audiofile(audio_path)
    audio_clip.close()
    return audio_path


def recognize_speech(audio_path: str) -> str:

    # Download the model and the processor
    processor = Wav2Vec2Processor.from_pretrained("jonatasgrosman/wav2vec2-large-xlsr-53-arabic")
    model = Wav2Vec2ForCTC.from_pretrained("jonatasgrosman/wav2vec2-large-xlsr-53-arabic")

    # Load the audio file using librosa (sample rate of 16 kHz).
    audio, rate = librosa.load(audio_path, sr=16000)

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


def summarize(transcript: str) -> str:
    summary = None
    # TODO: Implement logic
    return summary


if __name__ == "__main__":
    audio_path = convert_to_mp3(r"C:\Users\iWaheeb\Downloads\ramadan hackathon.mp4")
    transcript = recognize_speech(audio_path)
    print(transcript)
    # print(summarize(transcript))
