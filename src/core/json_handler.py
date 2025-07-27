import json
from datetime import datetime
import os
from pathlib import Path

# Path configuration
DATA_DIR = Path("data")
JSON_PATH = DATA_DIR / "library.json"
BACKUP_DIR = DATA_DIR / "backups"

# Database initialization structure
BASE_STRUCTURE = {
    "books": {},
    "users": {},
    "loans": [],
    "history": []
}

def create_directory():
    """Creates the directories if don't exist"""
    os.makedirs(DATA_DIR, exist_ok=True)
    os.makedirs(BACKUP_DIR, exist_ok=True)
    
def load_data():
    """
    Load data from the JSON file.
    If file doesn't exist creates one from the BASE STRUCTURE
    """
    create_directory()
    
    try:
        with open(JSON_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        # If the file doesn't exist or is corrupt
        save_data(BASE_STRUCTURE)
        return BASE_STRUCTURE.copy()
    
def save_data(data):
    """
    Save the data in the JSON file
    and creates a backup automatically

    Args:
        data (_type_): _description_
    """
    
    try:
        # Main save
        with open(JSON_PATH, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
        
        # Backup
        do_backup(data)
        return True
    except Exception as e:
        print(f"Saving error: {str(e)}")
        return False
    
def do_backup(data):
    """
    Creates a backup with timestamps in the backups folder
    Example: backup_20240913_1300.json

    Args:
        data (_type_): _description_
    """
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M")
    backup_path = BACKUP_DIR / f"backup_{timestamp}.json"
    
    try:
        with open(backup_path, "w", encoding="utf-8") as file:
            json.dump(data, file, indent=2, ensure_ascii=False)
    except Exception as e:
        print(f"Backup error: {str(e)}")