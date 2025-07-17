import datetime

class Book(object):
    def __init__(self, title, author, year, gender):
        self.ID = None
        self.title = title
        self.author = author
        self.year = year
        self.gender = gender
        self.status = "available"
        self.loaned_to = None
        
    def __str__(self):
        return f"New Book: {self.title} | {datetime.datetime.date()}"
        
    def change_status(self, new_status):
        self.status = new_status
        if new_status == "available":
            self.loaned_to = None
            
book = Book("my book", "me", 2019, "romance")
print(book)