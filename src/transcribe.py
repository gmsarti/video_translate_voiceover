from pathlib import Path
import subprocess

from src.paths import (
    TRANSFORMED_DATA_DIR,
    OUTPUT_DARA_DIR
)

def transcribe(
    input_audio:str = f"{TRANSFORMED_DATA_DIR}/audio_short_video_ptbr.mp3",
    output_text:str = f"{OUTPUT_DARA_DIR}/transcript_whisper_large"
):
    subprocess.run(
        [
            "whisper", 
            "--language", "pt", 
            "--word_timestamps", "True",
            "--model", "large", 
            "--output_dir", output_text, 
            input_audio
        ]
    )