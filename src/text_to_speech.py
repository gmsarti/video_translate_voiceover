from pathlib import Path
from src.paths import (
    TRANSFORMED_DATA_DIR,
    OUTPUT_DARA_DIR
)

from typing import List



def tts(
    input_list_of_text:List[str],
    path_folder_output_audio:str = f"{TRANSFORMED_DATA_DIR}/tts"
):
    
    from transformers import pipeline
    from datasets import load_dataset
    import soundfile as sf, torch

    synthesiser = pipeline("text-to-speech", "microsoft/speecht5_tts")

    embeddings_dataset = load_dataset("Matthijs/cmu-arctic-xvectors", split="validation")
    speaker_embedding = torch.tensor(embeddings_dataset[7306]["xvector"]).unsqueeze(0)
    # You can replace this embedding with your own as well.

    for i in range(len(input_list_of_text)):
        speech = synthesiser(input_list_of_text[i], forward_params={"speaker_embeddings": speaker_embedding})

        sf.write(f'{path_folder_output_audio}/part_{i}.wav', speech["audio"], samplerate=speech["sampling_rate"])


def stephen_hawking(
    input_text:str = f"{OUTPUT_DARA_DIR}/transcript_whisper_large",
    output_audio:str = f"{TRANSFORMED_DATA_DIR}/audio_short_video_en.mp3"
):
    import pyttsx3
    engine = pyttsx3.init()
    
    """ RATE"""
    rate = engine.getProperty('rate')   # getting details of current speaking rate
    engine.setProperty('rate', 140)     # setting up new voice rate

    """VOLUME"""
    volume = engine.getProperty('volume')   #getting to know current volume level (min=0 and max=1)
    engine.setProperty('volume',1.0)    # setting up volume level  between 0 and 1

    """VOICE"""
    voices = engine.getProperty('voices')       #getting details of current voice
    engine.setProperty('voice', voices[3].id)  #changing index, changes voices. o for male

    with open(input_text, 'r') as input_file:
        engine.save_to_file(input_file, f'{output_audio}/test.mp3')
        engine.runAndWait()
    
    
    
def bark_tts(
    input_text:str = f"{OUTPUT_DARA_DIR}/transcript_whisper_large",
    output_audio:str = f"{TRANSFORMED_DATA_DIR}/audio_short_video_en.mp3"
):
    from transformers import AutoProcessor, BarkModel
    import nltk  
    import numpy as np
    nltk.download('punkt')
    processor = AutoProcessor.from_pretrained("suno/bark")
    model = BarkModel.from_pretrained("suno/bark")

    with open(input_text, 'r') as input_file:
        script = input_file.read().replace("\n", " ").strip()
    sentences = nltk.sent_tokenize(script)
    
    SPEAKER = "v2/en_speaker_6"
    sample_rate = model.generation_config.sample_rate
    silence = np.zeros(int(0.25 * sample_rate))  # quarter second of silence

    pieces = []
    for sentence in sentences:
        
        inputs = processor(sentence, voice_preset=SPEAKER)
        audio_array = model.generate(**inputs)
        audio_array = audio_array.cpu().numpy().squeeze()
        
        pieces += [audio_array, silence.copy()]