from datetime import datetime
from src.core.json_handler import save_data
from email_validator import validate_email, EmailNotValidError

class User(object):
    user_counter = 0
    
    def __init__(self, name:str, sex:str, email:str, phone:str):
        self.id = f"USER-{User.user_counter:03d}"
        self.name = name
        self.sex = sex 
        self.email = email
        self.phone = phone
        self.active:bool = True
        self.joined_date = datetime.now().isoformat()
        self.borrowed_books = []
        
    def to_dict(self):
        """Converts the User object into a dictionary"""
        return {
            "id": self.id,
            "title": self.title,
            "author": self.author,
            "year": self.year,
            "gender": self.gender,
            "status": self.status,
            "loaned_to": self.loaned_to,
            "created_at": self.created_at
        }
    
    def borrow_book(self, book_id):
        if self.active:
            self.borrowed_books.append(book_id)
        else:
            print("This user is no longer active.")
        
    def return_book(self, book_id):
        self.borrowed_books.remove(book_id)
        
    def deactivate(self):
        if len(self.borrowed_books) == 0:
            self.active = False
            print(f"User: {self.id} is no longer active.")
        else:
            print(f"This user has to return some books!")
            
class UserManager(object):
    def __init__(self, database):
        self.database = database
        
    def register_user(self, name, sex, email, phone):
        new_user = User(name, sex, email, phone)
        
        user_dict = new_user.to_dict()
        self.database["users"][new_user.id] = user_dict
        save_data(self.database)
        
    def find_user_by_email(self, email):
        pass
        # Ver como implementar esta logica
        
    def get_user_activity(self):
        pass
        # Ver como implementar esta logica