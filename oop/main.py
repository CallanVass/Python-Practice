# from oop import Student
from oop import BankAccount
# from oop import Library
from oop import Book

# my_rectangle1 = Rectangle(5, 4)
# print(my_rectangle1.width)
# print(my_rectangle1.area())

# student = Student("Callan", 24)

# student.display_info()
# print(student.name)
# print(student.age)

Main
acc1 = BankAccount("Callan", 1000)
acc2 = BankAccount("Sarah", 1500)

acc1.deposit(1000)
acc2.deposit(2000)

acc1.check_balance()
acc2.check_balance()

acc1.transfer(1000, acc2)

acc1.check_balance()
acc2.check_balance()


# eragon = Book("Eragon", "Fiction", 617)

# eragon.set_name("Brisingr")

# book_dict = eragon.__dict__

# print(book_dict)

# my_library = Library()

# my_library.add_book("Sumtingwong", "CallanVass", 664)
# my_library.add_book("Sumtin666gwong", "Calla666nVass", 665)
# print(my_library.display_books())
