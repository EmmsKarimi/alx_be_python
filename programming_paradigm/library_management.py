# library_management.py

class Book:
    def __init__(self, title, author):
        """Initialize a book with title, author, and availability status."""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute to track availability

    def check_out(self):
        """Marks the book as checked out."""
        if not self._is_checked_out:
            self._is_checked_out = True
            return True
        return False  # Book is already checked out

    def return_book(self):
        """Marks the book as available again."""
        if self._is_checked_out:
            self._is_checked_out = False
            return True
        return False  # Book is already available

    def is_available(self):
        """Returns True if the book is available, otherwise False."""
        return not self._is_checked_out


class Library:
    def __init__(self):
        """Initialize the library with an empty list of books."""
        self._books = []

    def add_book(self, book):
        """Adds a new book to the library."""
        self._books.append(book)

    def check_out_book(self, title):
        """Checks out a book if available."""
        for book in self._books:
            if book.title == title and book.is_available():
                book.check_out()
                print(f"Checked out: '{title}'")
                return
        print(f"'{title}' is either not available or does not exist in the library.")

    def return_book(self, title):
        """Returns a book to the library."""
        for book in self._books:
            if book.title == title and not book.is_available():
                book.return_book()
                print(f"Returned: '{title}'")
                return
        print(f"'{title}' was not checked out or does not exist in the library.")

    def list_available_books(self):
        """Lists all available books in the library."""
        available_books = [book for book in self._books if book.is_available()]
        if available_books:
            for book in available_books:
                print(f"{book.title} by {book.author}")
        else:
            print("No books are available in the library.")
