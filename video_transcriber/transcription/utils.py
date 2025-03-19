import whisper
import os
from django.conf import settings

def transcribe_video(video_path):
    model = whisper.load_model("small")  # Choose model: tiny, base, small, medium, large
    result = model.transcribe(video_path)
    return result['text']
