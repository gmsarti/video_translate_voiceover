# IMPORTS
# import requests
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


# get_full_video()
    
# make_short_video()

# make_short_video_no_audio()

# get_mp3_from_mp4()

# transcribe()
# print("\n\nTranscribed")

# translation = simple_translation()
# print("\n\nTranslated")
# data = prepare_data_to_tts()

# tts(input_list_of_text = data)
# concatenate_audio()
print("\n\nAudio ready")

merge_video_audio()
