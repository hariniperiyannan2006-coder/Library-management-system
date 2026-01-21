# Library Management System
# Day 1: Menu and Program Flow

def show_menu():
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print("Add Book option selected (to be implemented)")
    elif choice == "2":
        print("View Books option selected (to be implemented)")
    elif choice == "3":
        print("Exiting the program. Thank you!")
        break
    else:
        print("Invalid choice. Please enter 1, 2, or 3.")