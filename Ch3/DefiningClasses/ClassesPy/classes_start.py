# Exercise file for Python for the C# Developer LinkedIn Learning course by Joe Marini

# TODO: Classes are defined using the class keyword
class Book:
    def __init__(self, title, author, price):
        self._title = title
        self._author = author
        self._price = price

    @property
    def title(self):
        return self._title

    def author(self):
        return self._author

    def price(self):
        return self._price

# TODO: create an instance of the class
b1 = Book("War and Peace", "Unknown", 12.00)
print(b1.author)