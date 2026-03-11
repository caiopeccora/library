from fake_data import loading_library_books, Book


library = loading_library_books()


while True:

    print("\nChoose an option:")
    print("1 - Add a book")
    print("2 - Search book")
    print("3 - Remove book")
    print("4 - Show available books")
    print("5 - Exit")

    option = input("Option: ")

    if option == "1":

        new_book = Book(
            len(library.books) + 1,
            input("Title: "),
            input("Author: "),
            int(input("Pages: ")),
            input("Publisher: "),
            input("Type: "),
            True
        )

        library.add_book(new_book)
        print("Book added.")

    elif option == "2":

        text = input("Search title or author: ")
        found = library.search_book(text)

        if found:
            for book in found:
                print(book)
        else:
            print("Book not found.")

    elif option == "3":

        try:
            book_id = int(input("Enter ID: "))
            library.remove_book(book_id)
        except ValueError:
            print("Invalid ID")

    elif option == "4":

        for book in library.books:
            if book.available:
                print(book)

    elif option == "5":

        print("Ending system.")
        break

    else:
        print("Invalid option.")