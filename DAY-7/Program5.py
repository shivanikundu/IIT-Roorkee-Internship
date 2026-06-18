#OOp : Library system with Book and Member classes
class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author
        self.issued = False

    def display(self):
        status = "Issued" if self.issued else "Available"
        print(f"Title: {self.title}, Author: {self.author}, Status: {status}")


class Member:
    def __init__(self, name):
        self.name = name

    def issue_book(self, book):
        if not book.issued:
            book.issued = True
            print(f"{self.name} issued '{book.title}'")
        else:
            print(f"Sorry! '{book.title}' is already issued.")

    def return_book(self, book):
        if book.issued:
            book.issued = False
            print(f"{self.name} returned '{book.title}'")
        else:
            print(f"'{book.title}' was not issued.")


# Creating books
book1 = Book("Python Programming", "Guido van Rossum")
book2 = Book("Data Structures", "Mark Allen")

# Creating member
member1 = Member("Varsha")

# Display books
book1.display()
book2.display()

# Issue a book
member1.issue_book(book1)

# Display updated status
book1.display()

# Return the book
member1.return_book(book1)

# Display updated status
book1.display()