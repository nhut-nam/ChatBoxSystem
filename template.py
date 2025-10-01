import os
from pathlib import Path
import logging

project_name = "ChatBoxSystem"

list_of_files = [
    ".github/workflows/.gitkeep",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/ingestion/__init__.py",
    f"src/{project_name}/preprocessing/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/embeddings/__init__.py",
    f"src/{project_name}/retrieval/__init__.py",
    f"src/{project_name}/generation/__init__.py",
    f"src/{project_name}/config/__init__.py",
    "config/config.yaml",
    "dvc.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb",
    "templates/index.html",
    "main.py"
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")

    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, "w") as f:
            pass
        logging.info(f"Creating empty file: {filepath}")
    else:
        logging.info(f"File already exists and is not empty: {filepath}")