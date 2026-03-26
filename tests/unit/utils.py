import os
import json
from datetime import datetime
import logging
from typing import Dict, Any, Optional

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

def load_json_file(file_path: str) -> Optional[Dict[str, Any]]:
    try:
        with open(file_path, 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        logger.error(f"File not found: {file_path}")
    except json.JSONDecodeError:
        logger.error(f"Invalid JSON in file: {file_path}")
    return None

def save_json_file(file_path: str, data: Dict[str, Any]) -> bool:
    try:
        with open(file_path, 'w') as file:
            json.dump(data, file, indent=4)
        return True
    except IOError:
        logger.error(f"Failed to save file: {file_path}")
        return False

def get_timestamp() -> str:
    return datetime.now().strftime("%Y-%m-%d_%H-%M-%S")

def ensure_directory_exists(directory_path: str) -> bool:
    if not os.path.exists(directory_path):
        try:
            os.makedirs(directory_path)
            return True
        except OSError:
            logger.error(f"Failed to create directory: {directory_path}")
            return False
    return True

def validate_email(email: str) -> bool:
    import re
    pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
    return re.match(pattern, email) is not None