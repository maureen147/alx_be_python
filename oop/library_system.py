class Book:
    def __init__(self,title,author):
        self.title = title
        self.author = author

    def __str__(self):
        return f"book: {self.title} by {self.author}"
    
class Ebook(Book):
    def __init__(self,title,author,file_size):
       super().__init__(title,author)
       self.file_size = file_size

    def __str__(self):
        return f"Ebook: {self.title} by {self.author}, file_size = {self.file_size}KB"

class Printbook(Book):
    def __init__(self,title,author,page_count):
        super().__init__(title,author)
        self.page_count = page_count
        
    def __str__(self):
         return f"Printbook:{self.title} by {self.author}, page_count = {self.page_count}KB"
    
class Library:

    def __init__(self):
        self.books =[]

    def add_book(self,book):
        self.books.append(book)

    def list_books(self):
          for book in self.books:
              print(book)