from src.paths import (
    OUTPUT_DARA_DIR
)
from googletrans import Translator


def simple_translation(
    path_input_text:str = f"{OUTPUT_DARA_DIR}/transcript_whisper_large/audio_short_video_ptbr.txt",
    path_output_text:str = f"{OUTPUT_DARA_DIR}/text_short_video_translated_en.txt"
):
    translator = Translator()
    final_translation = ""  # Initialize the string to store the accumulated translations

    with open(path_input_text, 'r') as input_file, open(path_output_text, 'w') as output_file:
        for line in input_file:
            translated_line = translator.translate(line, dest='en')
            final_translation += translated_line.text + "\n"  # Add newline for formatting

        output_file.write(final_translation)
        print("Translated text saved.")
        
    # Not the best practice to save and return the text, 
    # but here is really practical
    return final_translation