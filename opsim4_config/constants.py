
import os
from pathlib import Path

CONFIG_DIRECTORY_PATH = str(Path(__file__).parent.parent)
CONFIG_DIRECTORY_NAME = 'config_run/'  # The name of the configuration directory
CONFIG_DIRECTORY = os.path.join(CONFIG_DIRECTORY_PATH, CONFIG_DIRECTORY_NAME)
