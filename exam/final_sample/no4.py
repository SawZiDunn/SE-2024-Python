class LibraryBook:
    def __init__(self, title, author, available=True):
        self.title = title
        self.author = author
        self.available = available

    def borrow(self):
        if self.available:
            self.available = False
            print(f"{self.title} is borrowed!")
        else:
            print(f"{self.title} is currently not available.")

    def return_book(self):
        if not self.available:
            self.available = True
            print(f"{self.title} is returned!")
        else:
            print(f"{self.title} is not currently borrowed.\nYou cannot return a book that you haven't borrowed.")


class ReferenceBook(LibraryBook):
    # we add constructor inside child class only when we want to add additional behaviour or modify
    # the behaviour of the construct
    # if not, we can omit this, and python will automatically use the constructor of the parent class

    # So, the code below is not really necessary.
    # def __init__(self, title, author):
    #     super().__init__(title, author)

    def borrow(self):
        print(f"{self.title} cannot be borrowed!")

    def return_book(self):
        print(f"{self.title} cannot be returned since it cannot be borrowed in the first place.")

python = LibraryBook("Python", "Visit")
java = ReferenceBook("Java", "Sun")

python.borrow()
python.return_book()
java.borrow()
java.return_book()

