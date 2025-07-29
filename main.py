from src.core.books import Book, LibraryManager
from src.core.json_handler import load_data



def main():
    db = load_data()
    manager = LibraryManager(db)
    
    while True:
        option = main_menu()
        if option == "1":
            print("Add a new book:")
            title = input("Title: ")
            author = input("Author: ")
            year = int(input("Year: "))
            gender = input("Gender: ")
            book_id = manager.add_book(title, author, year, gender)  
            print(f"✅ Book added successfully! ID: {book_id}")

        elif option == "2":
            pass
        elif option == "3":
            pass
        elif option == "4":
            book_id = input("ID: ")
            manager.delete_book(book_id)
        elif option == "5":
            pass
        elif option == "6":
            pass
        elif option == "7":
            print("You exited the program.")
            break
        

def main_menu():
    print(" LIBRARY MANAGEMENT SYSTEM ")
    print(" _________________________ ")
    print("|1. Add book              |")
    print("|2. Find book by author   |")
    print("|3. Get book by ID        |")
    print("|4. Delete book           |")
    print("|____________*____________|")
    print("|5. See book list         |")
    print("|6. Generate report       |")
    print("|7. Quit                  |")
    print("|____________*____________|")
    option = input("Select a number: ")
    return option


if __name__ == "__main__":
    main()