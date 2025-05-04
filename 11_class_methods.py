# Class Methods
# Assignment:
# Create a class Book with a class variable total_books. Add a class method increment_book_count() to increase the count when a new book is added.




class Book():
    total_books = 0
    @classmethod
    def increment_book_count(cls):
        cls.total_books += 1
    def __init__(self):
        self.increment_book_count()
new_book1 = Book()
new_book2 = Book()
new_book3 = Book()
new_book4 = Book()
new_book5 = Book()
print(f"Total Books Added: {Book.total_books}")