import datetime

class Book(object):
    def __init__(self, title:str, author:str, year:int, gender:str):
        self.ID = None
        self.title = title
        self.author = author
        self.year = year
        self.gender = gender
        self.status = "available"
        self.loaned_to = None
        
    def __str__(self):
        return f"New Book: {self.title} | {datetime.datetime.date()}" # Acortar el formato de la fecha
        
    def change_status(self, new_status):
        self.status = new_status
        if new_status == "available":
            self.loaned_to = None
            
class LibraryManager(object):
    def __init__(self, database):
        self.database = database
    
    def add_book(self, book:Book):
        pass # Ver como implementar esta logica
    
    def find_by_author(self, author:str):
        pass # Ver como implementar esta logica
    
    def delete_book(self, id:int):
        pass # Ver como implementar esta logica
    
    def get_book_by_ID(self, id:int):
        pass # Ver como implementar esta logica