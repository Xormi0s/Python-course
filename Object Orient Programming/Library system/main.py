class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year
        
    def book_info(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}")
        
        
class FictionBook(Book):
    def __init__(self, title, author, year, genre):
        super().__init__(title, author, year)
        self.genre = genre
        
    def book_info(self):
        super().book_info()
        print(f"Genre: {self.genre}")
        
class NonFictionBook(Book):
    def __init__(self, title, author, year, topic):
        super().__init__(title, author, year)
        self.topic = topic
        
    def book_info(self):
        super().book_info()
        print(f"Topic: {self.topic}")
        
        
class Library():
    def __init__(self):
        self.books = []
        
    def add_book(self, book):
        self.books.append(book)
        
    def display_books(self):
        for book in self.books:
            book.book_info()
            print()
            
    def search_author(self, author):
        found_books = []
        for book in self.books:
            if book.author == author:
                found_books.append(book)
        if found_books:
            print(f"Books by: {author}")
            for book in found_books:
                book.book_info()
                print()
        else:
            print("No books found for this author!")
    
    def search_year(self, start_year, end_year):
        found_books = []
        for book in self.books:
            if start_year <= book.year <= end_year:
                found_books.append(book)
        if found_books:
            print(f"Books between {start_year} and {end_year}:")
            for book in found_books:
                book.book_info()
                print()
        else:
            print("No books found for these years!")
                
                
                

harry_potter = FictionBook("Harry Potter", "JK Rowling", 2005, "Magic")
cyberpunk = FictionBook("Cyberpunk 2077", "Jones", 2024, "Cyberpunk")

python_course = NonFictionBook("Python for beginners", "Josh", 2024, "Python programming")
java_course = NonFictionBook("Java OOP principles", "Jef", 2008, "Java programming")

library = Library()
library.add_book(harry_potter)
library.add_book(cyberpunk)
library.add_book(python_course)
library.add_book(java_course)


#library.display_books()
library.search_author("Jones")
library.search_year(2000, 2010)