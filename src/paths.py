from pathlib import Path
import os

PARENT_DIR = Path(__file__).parent.resolve().parent
DATA_DIR = PARENT_DIR / 'data'
RAW_DATA_DIR = DATA_DIR / 'raw'
TRANSFORMED_DATA_DIR = DATA_DIR / 'transformed'
OUTPUT_DARA_DIR = DATA_DIR / 'output'

