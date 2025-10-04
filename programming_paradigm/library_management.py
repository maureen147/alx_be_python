class Book:
    def __init__(self, title, author):
        """Initialize a Book with title, author, and set it as available"""
        self.title = title
        self.author = author
        self._is_checked_out = False  # Private attribute
    
    def check_out(self):
        """Mark the book as checked out"""
        self._is_checked_out = True
    
    def return_book(self):
        """Mark the book as returned/available"""
        self._is_checked_out = False
    
    def is_available(self):
        """Return True if the book is available, False otherwise"""
        return not self._is_checked_out
    
    def __str__(self):
        """Return string representation of the book"""
        return f"{self.title} by {self.author}"


class Library:
    def __init__(self):
        """Initialize a Library with an empty list of books"""
        self._books = []  # Private list to store books
    
    def add_book(self, book):
        """Add a book to the library"""
        self._books.append(book)
    
    def check_out_book(self, title):
        """Check out a book by title"""
        for book in self._books:
            if book.title == title:
                if book.is_available():
                    book.check_out()
                    return True
                else:
                    return False
        return False
    
    def return_book(self, title):
        """Return a book by title"""
        for book in self._books:
            if book.title == title:
                if not book.is_available():
                    book.return_book()
                    return True
                else:
                    return False
        return False
    
    def list_available_books(self):
        """List all available books in the library"""
        available_books = [book for book in self._books if book.is_available()]
        for book in available_books:
            print(book)
