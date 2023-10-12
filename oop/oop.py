class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height
    
    def area(self):
        return self.width * self.height
    
    def perimeter(self):
        return 2 * (self.width + self.height)

class Student:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def display_info(self):
        print(f"Name: {self.name} Age: {self.age}")

class BankAccount:
    def __init__(self, acc_num, balance):
        self.acc_num = acc_num
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else: 
            print("Insufficient funds.")

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title, author, isbn):
        self.books.append({"title": title, "author": author, "isbn": isbn})
    
    def display_books(self):
        for book in self.books:
            print(book)
    
    def find_book(self, title):
        for book in self.books:
            if book['title'] == title:
                return book
        return None