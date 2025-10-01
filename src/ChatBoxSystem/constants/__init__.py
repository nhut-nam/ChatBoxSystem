import os
from pathlib import Path
from dotenv import load_dotenv
load_dotenv()

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
API_KEY = os.getenv("GEMINI_API_KEY")