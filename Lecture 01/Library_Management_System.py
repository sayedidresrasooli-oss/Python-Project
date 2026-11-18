


class Person:
    def __init__(self, name, number):
        self.name = name
        self.number = number


class Librarian(Person):
    def __init__(self, name, number, id):
        super().__init__(name, number)
        self.id = id


class Book:
    def __init__(self, book_name, author, book_isbn):
        self.book_name = book_name
        self.author = author

class Loan(Book):
    def __init__(self, book_name, author, book_isbn):
        super().__init(book_name, author)
        print("This book has been borrowed")


class Library:
    def __init__(self, total_books, total_borrowed_books, total_member):
        self.total_books = total_books
        self.total_borrowed_books = total_borrowed_books
        self.total_member = total_member


l = Library(2000, 50, 12)
print("Total books in library: ",l.total_books)
print("Total borrowed books: ",l.total_borrowed_books)
print("Total number: ",l.total_member)


p = Person("Ahmad", 748141651)
print("name: ",p.name)
print("Number: ",p.number)

b = Book("Introduction to Python", "Y. Danil", "123456")
print("book name: ",b.book_name)
print("author: ",b.author)








