class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"{self.title} by {self.author}, {self.year}"

class Library:
    def __init__(self):
        self.books = []
        self.borrowed_books = []

    def add_book(self, book):
        self.books.append(book)

    def remove_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                return f"Le livre '{book_title}' a été supprimé."
        return f"Le livre '{book_title}' n'a pas été trouvé."

    def borrow_book(self, book_title):
        for book in self.books:
            if book.title == book_title:
                self.books.remove(book)
                self.borrowed_books.append(book)
                return f"Le livre '{book_title}' a été emprunté."
        return f"Le livre '{book_title}' n'est pas disponible."

    def return_book(self, book_title):
        for book in self.borrowed_books:
            if book.title == book_title:
                self.borrowed_books.remove(book)
                self.books.append(book)
                return f"Le livre '{book_title}' a été retourné."
        return f"Le livre '{book_title}' n'a pas été trouvé parmi les empruntés."

    def available_books(self):
        return [book.title for book in self.books]

    def borrowed_books_list(self):
        return [book.title for book in self.borrowed_books]

library = Library()

library.add_book(Book("Le Petit Prince", "Antoine de Saint-Exupéry", 1943))
library.add_book(Book("1984", "George Orwell", 1949))
library.add_book(Book("Les Misérables", "Victor Hugo", 1862))

print("Livres disponibles :", library.available_books())

print(library.borrow_book("1984"))
print("Livres disponibles après emprunt :", library.available_books())
print("Livres empruntés :", library.borrowed_books_list())

print(library.return_book("1984"))
print("Livres disponibles après retour :", library.available_books())
print("Livres empruntés après retour :", library.borrowed_books_list())

print(library.remove_book("Les Misérables"))
print("Livres disponibles après suppression :", library.available_books())
