from src.core.books import LibraryManager
from src.core.users import UserManager
from src.core.json_handler import load_data, log_activity, save_data
import sys
from colorama import init, Fore
import os
from email_validator import validate_email, EmailNotValidError
from src.core.interface import (
    main_menu,
    admin_menu,
    client_menu,
    book_menu,
    user_menu,
    loans_menu,
)
init(autoreset=True)

def main():
    def clear_screen():
        os.system('cls' if os.name == 'nt' else 'clear')
    
    # Cargar datos desde archivos separados
    books_data = load_data("books")
    users_data = load_data("users")
    active_loans = load_data("active_loans")
    loan_history = load_data("loan_history")

    # Inicializar gestores con sus respectivos datos
    book_manager = LibraryManager(books_data)
    user_manager = UserManager(users_data)
    
    def view_books(book_manager):
        """Shows all the books in a simple format"""
        books = book_manager.get_all_books()
        
        if not books:
            print("No books available in the library")
            return
        
        print(Fore.GREEN + "             Library 📚          ")
        for book in books:
            status = "Available" if book.status == "available" else f"Loaned to: {book.loaned_to}"
            print(Fore.BLUE + " __________________________________________")
            print(f"  ID: {book.id}                           ")
            print(f"  {Fore.BLUE + book.title}                ")
            print(f"  Author: {book.author}                   ")
            print(f"  Status: {status}                        ")
            print(Fore.BLUE + " __________________________________________") 
        print(Fore.YELLOW + "Total books:", len(books))
        option = input("🔙Back (Y/N): ").upper()
        return option

    # Registrar inicio del sistema
    log_activity("admin", "system_start", "Application initialized")
    while True:
        clear_screen()
        option = main_menu()
        if option == "1":
            # ----------------- Admin menu--------------------
            while True:
                clear_screen()
                option = admin_menu()
                if option == "1":
                    # ---------------- Book menu -----------------
                    while True: 
                        clear_screen()
                        option = book_menu()
                        if option == "1":
                            # Add new book
                            title = input("Title: ")
                            author = input("Author: ")
                            year = int(input("Year: "))
                            gender = input("Gender: ")
                            new_book = book_manager.add_book(title, author, year, gender)
                            save_data("books", books_data)
                            log_activity("admin", "new_book_added", f"✅ {new_book.title} added successfully with ID: {new_book.id}")
                        elif option == "2":
                            # Search books
                            term = input("Search term: ")
                            results = book_manager.search_books(term)
                            for book in results:
                                print(f"{book.id}: {book.title} ({book.author})")
                        elif option == "3":
                            # Remove book
                            book_id = input("Enter book ID: ")
                            book_manager.remove_book(book_id)
                            print("Book removed")
                            books_data = {k: v.to_dict() for k, v in book_manager.books.items()}
                            save_data("books", books_data)
                            log_activity("admin", "book_removed", f"Book {book_id} removed")
                        elif option == "4":
                            while True:
                                option = view_books(book_manager)
                                if option == "Y":
                                    break
                                elif option == "N":
                                    clear_screen()
                                    continue
                                else:
                                    print("Invalid choice!")
                                    pass
                        elif option == "5":
                            break
                        else:
                            print("Invalid choice!")
                elif option == "2":
                    # ----------------- User menu--------------------
                    while True:
                        clear_screen()
                        option = user_menu()
                        if option == "1":
                            # Register new user
                            pass
                        elif option == "2":
                            # Search users
                            pass
                        elif option == "3":
                            # View user details
                            pass
                        elif option == "4":
                            # Deactivate user
                            pass
                        elif option == "5":
                            # View all users
                            pass
                        elif option == "6":
                            # Generate user report
                            pass
                        elif option == "7":
                            break
                        else:
                            print("Invalid choice!")
                elif option == "3":
                    # --------------- Loans Menu ------------------
                    while True:
                        clear_screen()
                        option = loans_menu()
                        if option == "1":
                            # Create new loan
                            pass
                        elif option == "2":
                            # Process return
                            pass
                        elif option == "3":
                            # View active loans
                            pass
                        elif option == "4":
                            # View overdue loans
                            pass
                        elif option == "5":
                            # View loan history
                            pass
                        elif option == "6":
                            # Generate loan report
                            pass
                        elif option == "7":
                            break
                        else:
                            print("Invalid choice!")
                elif option == "4":
                    pass  # Change password
                elif option == "5":
                    break
                else:
                    print("Invalid choice!")
        elif option == "2":
            # -------------------- Client Menu --------------------
            while True:
                clear_screen()
                option = client_menu()
                if option == "1":
                    # ---------- Log in -----------
                    pass
                elif option == "2":
                    # ---------- Register ---------
                    pass
                elif option == "3":
                    break
                else:
                    print("Invalid choice!")
        # Quit the program
        elif option == "3":
            sys.exit("You exited the program!")
        else:
            print("Invalid choice!")


if __name__ == "__main__":
    main()
