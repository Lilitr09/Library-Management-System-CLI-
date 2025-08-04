from src.core.books import LibraryManager
from src.core.users import UserManager
from src.core.json_handler import load_data
import sys
from email_validator import validate_email, EmailNotValidError

def main():
    db = load_data()
    manager = LibraryManager(db)
    u_manager = UserManager(db)
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
            print("Register new user: ")
            name = input("Name: ")
            sex = input("Sex (F / M): ")
            try:
                email = validate_email(input("Email: "))
            except EmailNotValidError as e:
                print(f"Invalid email: {e}")
            phone = input("Phone number: ")
            new_user = u_manager.register_user(name, sex, email, phone)
            print(f"✅ User added successfully! ID: {new_user}")
            
                
        elif option == "0":
            sys.exit("You exited the program.")
        

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
    print("|____________*____________|")
    print("|7. Register new user     |")
    print("|8. See registerd users   |")
    print("|9. Loans                 |")
    print("|0. Quit                  |")
    print("|____________*____________|")
    option = input("Select a number: ")
    return option


if __name__ == "__main__":
    main()