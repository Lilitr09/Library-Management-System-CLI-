import colorama

def main_menu():
    print(" Welcome to Library Management System 📚 ")
    print(" _______________________________________ ")
    print("|                1. Admin               |")
    print("|                2. Client              |")
    print("|                3. Quit                |")
    print("|_______________________________________|")
    option = input("Select an option: ")
    return option

def admin_menu():
    print("              Admin Panel📋             ")
    print(" _______________________________________")
    print("|              1. Manage books          |")
    print("|              2. Manage users          |")
    print("|              3. Manage loans          |")
    print("|              4. Change password       |")
    print("|              5.🔙Go back              |")
    print("|_______________________________________|")
    option = input("Select an option: ")
    return option

def client_menu():
    print("               Client Panel 👤           ")
    print(" _______________________________________ ")
    print("|               1. Log in               |")
    print("|               2. Register             |")
    print("|               3.🔙Go back             |")
    print("|_______________________________________|")
    option = input("Select an option: ")
    return option

def book_menu():
    print("             Book Management📝          ")
    print(" _______________________________________")
    print("|            1. Add new book            |")
    print("|            2. Search books            |")
    print("|            3. Update book details     |")
    print("|            4. Remove book             |")
    print("|            5. View all books          |")
    print("|            6.🔙Back to Admin Panel    |")
    print("|_______________________________________|")
    option = input("Select an option: ")
    return option

def user_menu():
    print("             User Management📝          ")
    print(" _______________________________________")
    print("|            1. Register new user       |")
    print("|            2. Search users            |")
    print("|            3. View user details       |")
    print("|            4. Deactivate user         |")
    print("|            5. View all users          |")
    print("|            6. Generate user report    |")
    print("|            7.🔙Back to Admin Panel    |")
    print("|_______________________________________|")
    option = input("Select an option: ")
    return option

def loans_menu():
    print("             Loans Management📝          ")
    print(" _______________________________________")
    print("|            1. Create new loan         |")
    print("|            2. Process return          |")
    print("|            3. View active loans       |")
    print("|            4. View overdue loans      |")
    print("|            5. View loan history       |")
    print("|            6. Generate loan report    |")
    print("|            7.🔙Back to Admin Panel    |")
    print("|_______________________________________|")
    option = input("Select an option: ")
    return option





