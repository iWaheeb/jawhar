from moviepy import VideoFileClip
import os


def convert_to_mp3(video_path: str) -> str:
    file_name = os.path.basename(video_path)[:-4]
    audio_path = f"audio_cache/{file_name}.mp3"

    audio_clip = VideoFileClip(video_path).audio
    audio_clip.write_audiofile(audio_path)
    audio_clip.close()
    return audio_path


def recognize_speech(audio_path: str) -> str:
    transcript = None
    # TODO: Implement logic
    return transcript


def summarize(transcript: str) -> str:
    summary = None
    # TODO: Implement logic
    return summary


if __name__ == "__main__":
    audio_path = convert_to_mp3(r"C:\Users\iWaheeb\Downloads\sahoor.mp4")
    transcript = recognize_speech(audio_path)
    print(summarize(transcript))
