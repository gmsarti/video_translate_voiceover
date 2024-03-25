from pathlib import Path
from src.paths import (
    RAW_DATA_DIR,
    TRANSFORMED_DATA_DIR,
    OUTPUT_DARA_DIR,
)
from moviepy.video.io.ffmpeg_tools import ffmpeg_extract_subclip
from moviepy.editor import (
    VideoFileClip, 
    AudioFileClip, 
    CompositeAudioClip
)
from pydub import AudioSegment
from typing import List

# PATHS
URL_DOWNLOAD_FULL_VIDEO = "https://drive.google.com/file/d/1I8TRfJPufi9rJN5rSza2V3hK87X0yMX0/view?usp=drive_web"
full_video_path = RAW_DATA_DIR / 'case_ai.mp4'

def get_full_video():
    """IF NOT FULL VIDEO, DOWNLOAD"""
    
    try:
        if not any(RAW_DATA_DIR.glob("*.mp4")):
            print("Full video file NOT FIND")
            response = requests.get(URL_DOWNLOAD_FULL_VIDEO)
            open(full_video_path, 'wb').write(response.content)
        else:
            print('Video already there...')
    except Exception:
        print("URL to Download full video NOT WORKING")
  
    
def make_short_video(
    full_video_path:str = str(full_video_path),
    short_video_path:str = f"{TRANSFORMED_DATA_DIR}/short_video.mp4",
    start_time:int = 0, # Start at the beginning of the video
    end_time:int = 4 * 60 + 40 # 4 minutes and 40 seconds
):

    ffmpeg_extract_subclip(
        full_video_path,
        start_time, 
        end_time, 
        targetname= short_video_path
    )
    
    
def make_short_video_no_audio(
    inputfile:str = f"{TRANSFORMED_DATA_DIR}/short_video.mp4",
    output:str = f"{TRANSFORMED_DATA_DIR}/short_video_silent.mp4"
):
    # ffmpeg_extract_audio(
    #     inputfile = inputfile,
    #     output = output,
    # )
    video = VideoFileClip(inputfile)
    video_without_audio = video.without_audio()
    video_without_audio.write_videofile(output)
    

def prepare_data_to_tts(
    path_en_text:str = f"{OUTPUT_DARA_DIR}/text_short_video_translated_en.txt"
) -> List[str]:
    file = open(path_en_text, 'r')
    text_content = file.read()
    file.close()
    list_of_phrases = text_content.splitlines()
    phrases_to_tts = []
    last_phrase = 0

    while last_phrase < len(list_of_phrases):
        sum_of_phrases = ""
        while len(sum_of_phrases)<500:
            try:
                sum_of_phrases += f" {list_of_phrases[last_phrase]}"
                last_phrase += 1
            except Exception as e:
                print(e)
                print("Finishin process...")
                break
        phrases_to_tts.append(sum_of_phrases)
    
    return phrases_to_tts


def get_mp3_from_mp4(
    path_video:str = f"{TRANSFORMED_DATA_DIR}/short_video.mp4",
    path_export_audio:str = f"{TRANSFORMED_DATA_DIR}/audio_short_video_ptbr.mp3",
):
    audio_short_video_ptbr = AudioSegment.from_file(path_video, "mp4")
    audio_short_video_ptbr.export(path_export_audio, format="mp3")
    
def concatenate_audio(
    path_input_folder:str = TRANSFORMED_DATA_DIR / "tts",
    path_output_file:str = f"{TRANSFORMED_DATA_DIR}/tts/full_audio_en.wav",
):
    wav_files = sorted(path_input_folder.glob("part_*.wav"))
    if not wav_files:
        print("No .wav files found in the directory!")
    else:
        # Initialize an empty audio segment
        combined_sound = AudioSegment.empty()

        # Iterate through the sorted files and concatenate
        for file in wav_files:
            sound = AudioSegment.from_wav(file)
            combined_sound += sound

        # Export the combined audio
        combined_sound.export(path_output_file, format="wav")

        print(f"Concatenated audio saved as {path_output_file}")


def merge_video_audio(
    path_video_input:str = f"{TRANSFORMED_DATA_DIR}/short_video_silent.mp4",
    path_audio_input:str = f"{TRANSFORMED_DATA_DIR}/tts/full_audio_en.wav",
    path_video_output:str = f"{OUTPUT_DARA_DIR}/short_video_en.mp4",
):
    
    video_clip = VideoFileClip(path_video_input)
    audio_clip = AudioFileClip(path_audio_input)
    video_clip = video_clip.set_audio(audio_clip) 
    video_clip.write_videofile(path_video_output)