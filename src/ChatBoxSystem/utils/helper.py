import os
import yaml
from ensure import ensure_annotations
from click import Path
from ChatBoxSystem import logger
from box import ConfigBox

@ensure_annotations
def read_yaml(path_to_yaml: Path) -> dict:
    """Reads a yaml file and returns the contents as a dictionary.

    Args:
        path_to_yaml (Path): Path to the yaml file.
    Returns:
        dict: Contents of the yaml file as a dictionary.
    """
    try:
        with open(path_to_yaml, 'r') as yaml_file:
            content = yaml.safe_load(yaml_file)
            logger.info(f"YAML file {path_to_yaml} loaded successfully.")
            return ConfigBox(content)
    except BoxValueError as e:
        logger.error(f"Error converting YAML content to ConfigBox: {e}")
        return ConfigBox({})
    except Exception as e:
        logger.error(f"Error loading YAML file {path_to_yaml}: {e}")
        return ConfigBox({})
    
@ensure_annotations
def create_directories(path_to_directories: list, verbose=True):
    """Creates directories if they do not exist.

    Args:
        path_to_directories (list): List of directory paths to create.
        verbose (bool, optional): If True, logs the creation of directories. Defaults to True.
    """
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        if verbose:
            logger.info(f"Directory created at: {path}")