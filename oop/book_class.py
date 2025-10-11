class Book:
    def __init__(self, title, author, year):
        """Constructor: Initialize the book attributes"""
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        """User-friendly display of the book"""
        return f"{self.title} by {self.author}, published in {self.year}"

    def __repr__(self):
        """Developer-friendly representation that can recreate the object"""
        return f"Book('{self.title}', '{self.author}', {self.year})"

    def __del__(self):
        """Destructor: Message when the book is deleted"""
        print(f"Deleting {self.title}")
