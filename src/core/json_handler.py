import json
from datetime import datetime
import os
from pathlib import Path

# Path configuration
DATA_DIR = Path("data")
FILES = {
    "books": DATA_DIR / "books.json",
    "users": DATA_DIR / "users.json",
    "active_loans": DATA_DIR / "active_loans.json",
    "loan_history": DATA_DIR / "loan_history.json",
    "admin_passwords": DATA_DIR / "admin_passwords.json",
    "activity_log": DATA_DIR / "activity_log.json"
}
BACKUP_DIR = DATA_DIR / "backups"

# Database initialization structure
DEFAULT_STRUCTURES = {
    "books": {},
    "users": {},
    "active_loans": [],
    "loan_history": [],
    "admin_passwords": {},
    "activity_log": []
}
def create_directory():
    """Creates the directories if don't exist"""
    DATA_DIR.mkdir(exist_ok=True)
    for file_path in FILES.values():
        file_path.parent.mkdir(exist_ok=True, parents=True)
    
def load_data(file_key):
    """
    Loads data from an specific file
    """
    create_directory()
    file_path = FILES[file_key]
    
    try:
        if file_path.exists():
            with open(file_path, "r", encoding="utf-8") as f:
                return json.load(f)
    except (json.JSONDecodeError, IOError) as e:
        print(f"Error loading {file_key}: {str(e)}")
        
    # If the file does not exist or there is an error, return default structure.
    return DEFAULT_STRUCTURES[file_key].copy()
    
def save_data(file_key, data):
    """
    Save the data in an specific JSON file
    """
    
    try:
        file_path = FILES[file_key]
        with open(file_path, "w", encoding="utf-8") as f:
            json.dump(data, f, indent=2, ensure_ascii=False)
            return True
    except (IOError, TypeError) as e:
        print(f"Error saving {file_key}: {str(e)}")
        return False
    
def log_activity(user_id, action, details=""):
    "Registers an activity in the system log"
    log = load_data("activity_log")
    timestamp = datetime.now().isoformat()
    
    log.append({
        "timestamp": timestamp,
        "user_id": user_id,
        "action": action,
        "details": details
    })
    
    save_data("activity_log", log)

def update_admin_password(new_password_hash):
    """Updates the admin password"""
    passwords = load_data("admin_passwords")
    
    # If first password
    if not passwords:
        passwords = {"current": "", "history": []}
    
    # Update history
    if passwords["current"]:
        passwords["history"].append({
            "hash": passwords["current"],
            "changed_at": datetime.now().isoformat()
        })
    
    # 10 entries
    passwords["history"] = passwords["history"][-10:]
    
    # Update password
    passwords["current"] = new_password_hash
    
    save_data("admin_passwords", passwords)
    
    # Register activity
    log_activity("admin", "password_change", "Admin password updated")

def create_loan(loan_data):
    """Crea un nuevo préstamo"""
    active_loans = load_data("active_loans")
    active_loans.append(loan_data)
    save_data("active_loans", active_loans)
    
    # Registrar actividad
    log_activity(
        user_id=loan_data.get("admin_id", "system"),
        action="create_loan",
        details=f"Book: {loan_data['book_id']} to User: {loan_data['user_id']}"
    )

def complete_loan(loan_id):
    """Mueve un préstamo de activos a historial"""
    active_loans = load_data("active_loans")
    loan_history = load_data("loan_history")
    
    # Encontrar y mover el préstamo
    for i, loan in enumerate(active_loans):
        if loan["id"] == loan_id:
            completed_loan = active_loans.pop(i)
            completed_loan["returned_at"] = datetime.now().isoformat()
            loan_history.append(completed_loan)
            break
    
    save_data("active_loans", active_loans)
    save_data("loan_history", loan_history)
    
    # Registrar actividad
    log_activity(
        user_id=completed_loan.get("admin_id", "system"),
        action="complete_loan",
        details=f"Loan ID: {loan_id}"
    )

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