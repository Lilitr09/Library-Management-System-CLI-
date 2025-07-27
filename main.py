from src.core.books import Book, LibraryManager
from src.core.json_handler import load_data, save_data, do_backup, create_directory
import colorama


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
            new_book = manager.add_book(title, author, year, gender)
            save_data(new_book)
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