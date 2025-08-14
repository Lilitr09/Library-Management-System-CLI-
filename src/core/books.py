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
        self.last_updated = self.created_at
        
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
            "created_at": self.created_at,
            "last_updated": self.last_updated
        }
    def update(self, **kwargs):
        """Actualiza propiedades del libro"""
        allowed_fields = {"title", "author", "year", "gender", "status"}
        for field, value in kwargs.items():
            if field in allowed_fields:
                setattr(self, field, value)
        self.last_updated = datetime.now().isoformat()
            
class LibraryManager(object):
    def __init__(self, books_data:dict):
        """
        :param books_data: Diccionario de libros cargado desde JSON
        """
        self.books_data = books_data
        self.books = {}
        
        # Convertir diccionarios a objetos Book
        for book_id, book_dict in books_data.items():
            self._create_book_from_dict(book_dict)
        
        # Inicializar contador con el máximo ID existente
        self._initialize_counter()
        
    def _create_book_from_dict(self, book_dict: dict):
        """Crea un objeto Book desde un diccionario"""
        book = Book(
            title=book_dict["title"],
            author=book_dict["author"],
            year=book_dict["year"],
            gender=book_dict["gender"]
        )
        
        # Sobreescribir propiedades con valores almacenados
        book.id = book_dict["id"]
        book.status = book_dict["status"]
        book.loaned_to = book_dict["loaned_to"]
        book.created_at = book_dict["created_at"]
        book.last_updated = book_dict["last_updated"]
        
        self.books[book.id] = book
    
    def _initialize_counter(self):
        """Inicializa el contador de libros con el máximo ID existente"""
        if not self.books:
            Book.book_counter = 0
            return
            
        try:
            # Extraer el número secuencial de los IDs (ej: "202309-001" -> 1)
            max_id = max(int(book.id.split('-')[1]) for book in self.books.values())
            Book.book_counter = max_id
        except (ValueError, IndexError):
            Book.book_counter = len(self.books)
    
    def add_book(self, title:str, author:str, year:int, gender:str):
        new_book = Book(title, author, year, gender)
        
        self.books[new_book.id] = new_book
        # Actualizar datos persistentes
        self.books_data[new_book.id] = new_book.to_dict()
        return new_book
    def get_book(self, book_id: str) -> Book:
        return self.books.get(book_id)
    
    # def update_book(self, book_id: str, **updates) -> bool:
    #     book = self.get_book(book_id)
    #     if not book:
    #         return False
    #     book.update(**updates)
    #     return True
    
    def search_books(self, search_term: str) -> list:
        term = search_term.lower()
        results = []
        for book in self.books.values():
            if (term in book.title.lower() or 
                term in book.author.lower() or 
                term in book.gender.lower()):
                results.append(book)
        return results
    
    def loan_book(self, book_id: str, user_id: str) -> bool:
        book = self.get_book(book_id)
        if not book or book.status != "available":
            return False
        book.status = "loaned"
        book.loaned_to = user_id
        book.last_updated = datetime.now().isoformat()
        return True
    
    def return_book(self, book_id: str) -> bool:
        book = self.get_book(book_id)
        if not book or book.status != "loaned":
            return False
        book.status = "available"
        book.loaned_to = None
        book.last_updated = datetime.now().isoformat()
        return True
    
    def to_dict(self):
        """Convierte todos los libros a diccionarios para almacenamiento"""
        return {book_id: book.to_dict() for book_id, book in self.books.items()}
        
    def remove_book(self, book_id):
        if book_id not in self.books:
            raise ValueError(f"Book with ID:{book_id} does not exist.")
        
        book = self.books[book_id]
        if book.status != "available":
            raise ValueError(f"Book: {book_id} cannot be removed | Status: {book.staus}")
        
        del self.books[book_id]
    
    def get_all_books(self) -> list:
        return list(self.books.values())