## Library Management System
# Day 2: Add Book Feature

books = []  # List to store book details

def show_menu():
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Exit")

while True:
    show_menu()
    choice = input("Enter your choice (1-3): ")

    if choice == "1":
        print("\n--- Add Book ---")
        book_id = input("Enter Book ID: ")
        book_name = input("Enter Book Name: ")
        author = input("Enter Author Name: ")

        book = {
            "id": book_id,
            "name": book_name,
            "author": author,
            "status": "Available"
        }

        books.append(book)
        print("Book added successfully!")

    elif choice == "2":
        print("\n--- View Books ---")
        if not books:
            print("No books available.")
        else:
            for book in books:
                print(
                    f"ID: {book['id']} | "
                    f"Name: {book['name']} | "
                    f"Author: {book['author']} | "
                    f"Status: {book['status']}"
                )

    elif choice == "3":
        print("Exiting the program. Thank you!")
        break

    else:
        print("Invalid choice. Please enter 1, 2, or 3.")
