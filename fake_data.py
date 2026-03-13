from faker import Faker
import random


class Book:
    def __init__(self, id, title, author, pages, publisher, book_type, available=True):
        self.id = id
        self.title = title
        self.author = author
        self.pages = pages
        self.publisher = publisher
        self.book_type = book_type
        self.available = available

    def __str__(self):
        return (
        f"{self.id}  "
        f"{self.title} by {self.author} "
        f"({self.pages} pages) "
        f"[{self.publisher} - {self.book_type}] "
        f"{'Available' if self.available else 'Not Available'}"
    )


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_id):
        for i, book in enumerate(self.books):
            if book.id == book_id:
                removed = self.books.pop(i)
                print(f"Book '{removed.title}' removed.")
                return True
        print("Book not found.")
        return False

    def search_book(self, text):
        text = text.lower()
        found = []

        for book in self.books:
            if text in book.title.lower() or text in book.author.lower():
                found.append(book)

        return found


def loading_library_books():

    fake = Faker()

    book_types = [
        "Fiction", "Non-Fiction", "Romance",
        "Science Fiction", "Fantasy",
        "Mystery", "Biography"
    ]

    publishers = {
        "Saraiva": 300,
        "Pagina": 500,
        "editoria": 640,
        "editora legal": 940
    }

    library = Library()
    book_id = 1

    for publisher, min_pages in publishers.items():

        for _ in range(200):

            book = Book(
                book_id,
                fake.sentence(nb_words=3),
                fake.name(),
                random.randint(min_pages, min_pages + 200),
                publisher,
                random.choice(book_types),
                random.choice([True, False])
            )

            library.add_book(book)
            book_id = random.randint(0, 100000)

    return library

#1