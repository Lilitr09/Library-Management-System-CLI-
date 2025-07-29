from datetime import datetime
from src.core.json_handler import save_data


class Book(object):
    book_counter = 0
    
    def __init__(self, title:str, author:str, year:int, gender:str):
        # Generate unique ID based on the date a book was added and a sequential number
        today = datetime.now().strftime("%Y%m")
        Book.book_counter += 1
        
        self.id = f"{today}-{Book.book_counter:03d}"
        self.title = title
        self.author = author
        self.year = year
        self.gender = gender
        self.status = "available"
        self.loaned_to = None
        self.created_at = datetime.now().isoformat()
        
    def __str__(self):
        return f"New Book: {self.title} | Added: {self.created_at}" 
        
    def change_status(self, new_status):
        self.status = new_status
        if new_status == "available":
            self.loaned_to = None
    def to_dict(self):
        """Converts the Book object into a dictionary"""
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
            
class LibraryManager(object):
    def __init__(self, database):
        self.database = database
    
    def add_book(self, title:str, author:str, year:int, gender:str):
        new_book = Book(title, author, year, gender)
        
        book_dict = new_book.to_dict()
        self.database["books"][new_book.id] = book_dict
        save_data(self.database)
        
    
    def find_by_author(self, author:str):
        pass # Ver como implementar esta logica
    
    def delete_book(self, id:int):
        pass # Ver como implementar esta logica
    
    def get_book_by_ID(self, id:int):
        pass # Ver como implementar esta logica