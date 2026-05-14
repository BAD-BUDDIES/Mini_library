# Bad Buddies Mini Library 
library = {
    "The Song of Achilles": {"status": "Available", "description": "A tragic love story between Achilles and Patroclus set in Greek mythology."},
    "No Longer Human": {"status": "Available", "description": "A dark novel about alienation and the struggle of fitting into society."},
    "The Alchemist": {"status": "Borrowed", "description": "A philosophical story about following your dreams and personal legend."},
"The Great Gatsby": {"status": "Available", "description": "A classic novel about the American Dream and the decadence of the Jazz Age."}
}
print("Welcome to Bad Buddies Mini Library!")

while True:
    print("\n---- MENU ----")
    print("1. View Books")
    print("2. Add Book")
    print("3. Borrow Book")
    print("4. Return Book")
    print("5. Delete Book")
    print("6. Exit")

    choice = input("\nOption(1-6): ")

    if choice == "1":
        print("\nCURRENT BOOKS:")
        for book, info in library.items():
            print(f" - {book}")
            print(f"   Status: {info['status']}")
            print(f"   Description: {info['description']}")

    elif choice == "2":
        print("\n---Add a Book---")
        title = input("Book title: ")
        desc = input("Book description: ")
        library[title] = {"status": "Available", "description": desc}
        print(f"'{title}' is added to the library.")

    elif choice == "3":
        print("\n---BORROW A BOOK---")
        print("AVAILABLE BOOKS:")
        available_books = [book for book, info in library.items() if info["status"] == "Available"]

        if available_books:
            for book in available_books:
                print(f" - {book}")

            title = input("Book title: ")

            if title in library:
                if library[title]["status"] == "Available":
                    library[title]["status"] = "Borrowed"
                    print(f"You've borrowed '{title}'.")
                else:
                    print("Sorry, that book is already borrowed.")
            else:
                print("That book doesn't exist in this library.")
        else:
            print("No books are currently available.")

    elif choice == "4":
        print("\nBORROWED BOOKS:")
        borrowed_books = [book for book, info in library.items() if info["status"] == "Borrowed"]

        if borrowed_books:
            for book in borrowed_books:
                print(f" - {book}")

            title = input("\nBook title: ")

            if title in library:
                if library[title]["status"] == "Borrowed":
                    library[title]["status"] = "Available"
                    print(f"You've returned '{title}'.")
                else:
                    print("That book is already available.")
            else:
                print("That book doesn't exist.")
        else:
            print("No books are currently borrowed.")

    elif choice == "5":
        print("\n---DELETE A BOOK---")
        print("ALL BOOKS:")
        for book in library:
            print(f" - {book}")

        title = input("Book title: ")

        if title in library:
            del library[title]
            print(f"'{title}' has been removed from the library.")
        else:
            print("That book does not exist.")

    elif choice == "6":
        print("Thank you, Please visit us again!")
        break

    else:
        print("Invalid choice, try again.")