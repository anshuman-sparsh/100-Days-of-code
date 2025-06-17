# 🔹 1. Book Class
# Create a class Book with attributes: title, author, and year.
# Create an object and print its details using a method.




class book:
    def __init__(self,title,author,year):
        self.title = title
        self.author = author
        self.year = year

    def show_books(self):
        print(f"Title: {self.title}")
        print(f"Author: {self.author}")
        print(f"Year: {self.year}\n")

my_book = book("Wings of Fire", "A.P.J. Abdul Kalam", 1999)
my_book1 = book("Build An Epic Career", "Ankur Warikoo", 2025)
my_book.show_books()
my_book1.show_books()