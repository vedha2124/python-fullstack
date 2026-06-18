# Week 2 - library system
# practising classes again. A Library holds a bunch of Book objects.
# you can add, search, borrow and return books.

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.is_borrowed = False   # every new book starts off available

    def status(self):
        # just a little helper so I can print available/borrowed easily
        if self.is_borrowed:
            return "borrowed"
        else:
            return "available"


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author):
        self.books.append(Book(title, author))
        print("Added:", title, "by", author)

    def find_book(self, title):
        # look for an exact title match (ignoring case), returns None if not found
        for book in self.books:
            if book.title.lower() == title.lower():
                return book
        return None

    def search(self, keyword):
        keyword = keyword.lower()
        found = False
        for book in self.books:
            # match on either the title or the author
            if keyword in book.title.lower() or keyword in book.author.lower():
                print("-", book.title, "by", book.author, "(" + book.status() + ")")
                found = True
        if not found:
            print("No books matched that search.")

    def borrow(self, title):
        book = self.find_book(title)
        if book is None:
            print("That book is not in the library.")
        elif book.is_borrowed:
            print("Sorry, that book is already borrowed.")
        else:
            book.is_borrowed = True
            print("You borrowed:", book.title)

    def return_book(self, title):
        book = self.find_book(title)
        if book is None:
            print("That book is not in the library.")
        elif not book.is_borrowed:
            print("That book was not borrowed.")   # can't return something nobody took
        else:
            book.is_borrowed = False
            print("You returned:", book.title)

    def show_all(self):
        if len(self.books) == 0:
            print("The library is empty.")
            return
        print("\n--- All Books ---")
        for book in self.books:
            print("-", book.title, "by", book.author, "(" + book.status() + ")")


def main():
    library = Library()
    # start with a couple of books so the menu isn't empty
    library.add_book("The Hobbit", "Tolkien")
    library.add_book("Python Basics", "Guido")

    while True:
        print("\n===== Library Menu =====")
        print("1. Add book")
        print("2. Show all books")
        print("3. Search book")
        print("4. Borrow book")
        print("5. Return book")
        print("6. Exit")

        choice = input("Choose an option (1-6): ")

        if choice == "1":
            title = input("Book title: ")
            author = input("Author: ")
            library.add_book(title, author)
        elif choice == "2":
            library.show_all()
        elif choice == "3":
            keyword = input("Search for: ")
            library.search(keyword)
        elif choice == "4":
            title = input("Title to borrow: ")
            library.borrow(title)
        elif choice == "5":
            title = input("Title to return: ")
            library.return_book(title)
        elif choice == "6":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Please type 1-6.")


main()
