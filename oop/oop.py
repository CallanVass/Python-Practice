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
    def __init__(self, name, balance):
        self.name = name
        self.balance = balance
    
    def deposit(self, amount):
        self.balance += amount
    
    def check_balance(self):
        return print(self.balance)

    def withdraw(self, amount):
        if amount <= self.balance:
            self.balance -= amount
        else: 
            print("Insufficient funds.")

    def transfer(self, trans_amount, name):
        if trans_amount <= self.balance:
            self.balance -= trans_amount
            if isinstance(name, BankAccount):
                name.deposit(trans_amount)
                print("")
            else: 
                print("Please enter a valid name.")
        else: 
            print("Insufficient funds for transfer.")




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
    

class Book:
    def __init__ (self, name, genre, pages):
        self.name = name
        self.genre = genre
        self.pages = pages
        
    def set_name(self, new_name):
        if not isinstance(new_name, str) or len(new_name) > 20:
            print("Name must be a string and below 20 characters")
        else:
            self.name = new_name
    

class Player:
    pass

class Board:
    def __init__(self, matrix):
        self.matrix = [["", "", ""],
                       ["", "", ""],
                       ["", "", ""]]
   
    
        


#Tick Tack Toe

#Hash class, 3 rows (matrix) initialised
#rounds/tally for each time someone wins
#Player objects
    