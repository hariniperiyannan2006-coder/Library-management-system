## Library Management System
# Day 2: Add Book Feature

books = []  # List to store book details

def show_menu():
    print("\n===== Library Management System =====")
    print("1. Add Book")
    print("2. View Books")
    print("3. Search Book")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Delete Book")
    print("7. Exit")
def load_books():
    try:
        with open("library_data.txt", "r") as file:
            for line in file:
                id, name, author, status = line.strip().split(",")
                books.append({
                    "id": id,
                    "name": name,
                    "author": author,
                    "status": status
                })
    except FileNotFoundError:
        pass
def save_books():
    with open("library_data.txt", "w") as file:
        for book in books:
            file.write(
                f"{book['id']},{book['name']},{book['author']},{book['status']}\n"
            )   
def search_book():
    search_name = input("Enter book name to search: ")
    found = False
    for book in books:
        if book["name"].lower() == search_name.lower():
            print(
                f"Book Found → ID: {book['id']}, "
                f"Author: {book['author']}, "
                f"Status: {book['status']}"
            )
            found = True
            break
    if not found:
        print("Book not found.")
def issue_book():
    book_id = input("Enter Book ID to issue: ")
    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Available":
                book["status"] = "Issued"
                save_books()
                print("Book issued successfully.")
            else:
                print("Book is already issued.")
            return
    print("Book ID not found.")
def delete_book():
    book_id = input("Enter Book ID to delete: ")

    for book in books:
        if book["id"] == book_id:
            books.remove(book)
            save_books()
            print("Book deleted successfully.")
            return
    print("Book ID not found.")
def return_book():
    book_id = input("Enter Book ID to return: ")
    for book in books:
        if book["id"] == book_id:
            if book["status"] == "Issued":
                book["status"] = "Available"
                save_books()
                print("Book returned successfully.")
            else:
                print("Book was not issued.")
            return
    print("Book ID not found.")
load_books()
while True:
    show_menu()
    choice = input("Enter your choice (1-7): ")

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
        save_books()
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
        print("\n--- Search Book ---")
        search_book()

    elif choice == "4":
        print("\n--- Issue Book ---")
        issue_book()

    elif choice == "5":
        print("\n--- Return Book ---")
        return_book()

    elif choice == "6":
         print("\n--- Delete Book ---")
         delete_book()

    elif choice == "7":
         print("Exiting the program. Thank you!")
         break
        
    else:
        print("Invalid choice. Please enter 1 to 7.")
        



