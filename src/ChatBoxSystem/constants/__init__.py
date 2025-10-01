import os
from pathlib import Path

CONFIG_FILE_PATH = Path("config/config.yaml")
PARAMS_FILE_PATH = Path("params.yaml")
API_KEY = os.getenv("GEMINI_API_KEY")