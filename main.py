# IMPORTS
import os
from src.data import (
    get_full_video,
    make_short_video,
    make_short_video_no_audio,
    get_mp3_from_mp4,
    prepare_data_to_tts,
    concatenate_audio,
    merge_video_audio
)
from src.transcribe import transcribe
from src.translate import simple_translation
from src.text_to_speech import tts


import os

def create_folders(folder_paths):
  """
  Checks if the specified folders exist and creates them if necessary.

  Args:
      folder_paths: A list of folder paths to check and create.
  """
  for folder_path in folder_paths:
    if not os.path.exists(folder_path):
      os.makedirs(folder_path)
      print(f"Created folder: {folder_path}")

folders_to_create = ["data", "data/raw", "data/transformed", "data/output"]
create_folders(folders_to_create)

get_full_video()
print("\n\nVideo loaded...")
    
make_short_video()
make_short_video_no_audio()
print("\n\nShort videos crateded...")

get_mp3_from_mp4()
print("\n\nGot audio...")

transcribe()
print("\n\nTranscribed")

translation = simple_translation()
print("\n\nTranslated")
data = prepare_data_to_tts()

tts(input_list_of_text = data)
concatenate_audio()
print("\n\nAudio ready")

merge_video_audio()
print("\n\nFinal video ready")

