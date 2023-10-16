# from oop import Student
from oop import BankAccount
from oop import Library
from oop import Book

# my_rectangle1 = Rectangle(5, 4)
# print(my_rectangle1.width)
# print(my_rectangle1.area())

# student = Student("Callan", 24)

# student.display_info()
# print(student.name)
# print(student.age)

# Main
# acc1 = BankAccount("Callan", 1000)
# acc2 = BankAccount("Sarah", 1500)

# acc1.deposit(1000)
# acc2.deposit(2000)

# acc1.check_balance()
# acc2.check_balance()

# acc1.transfer(1000, acc2)

# acc1.check_balance()
# acc2.check_balance()


# eragon = Book("Eragon", "Fiction", 617)

# eragon.set_name("Brisingr")



# print(eragon.__dict__)

# my_library = Library()

# my_library.add_book("Sumtingwong", "CallanVass", 664)
# my_library.add_book("Sumtin666gwong", "Calla666nVass", 665)
# print(my_library.display_books())


#Tick Tack Toe

#Hash class, 3 rows (matrix) initialised
#rounds/tally for each time someone wins
#Player objects
import random

game_matrix = [["1", "2", "3"],
                ["4", "5", "6"],
                ["7", "8", "9"]]

winning_dict = {
    "Player_1_wins": 0,
    "Player_2_wins": 0
}

print("Welcome to TICK TACK TOE!")
player_1 = input("Please enter the name of the first Player: ")
player_2 = input("Please enter the second Player: ")



print(f"{player_1} will be going first! They are 'x'")


for line in game_matrix:
    print(line)



def player_1_loop():
    anchor = True
    while anchor:
        move = input("Please enter the number you wish to place your mark on: ")
        match move:
            case "1":
                game_matrix[0][0] = "X"
                for line in game_matrix:
                    print(line)
                return
            case "2":
                game_matrix[0][1] = "X"
                for line in game_matrix:
                    print(line)
                return
            case "3":
                game_matrix[0][2] = "X"
                for line in game_matrix:
                    print(line)
                return
            case "4":
                game_matrix[1][0] = "X"
                for line in game_matrix:
                    print(line)
                return
            case "5":
                game_matrix[1][1] = "X"
                for line in game_matrix:
                    print(line)
                return
            case "6":
                game_matrix[1][2] = "X"
                for line in game_matrix:
                    print(line)
                return
            case "7":
                game_matrix[2][0] = "X"
                for line in game_matrix:
                    print(line)
                return
            case "8":
                game_matrix[2][1] = "X"
                for line in game_matrix:
                    print(line)
                return
            case "9":
                game_matrix[2][2] = "X"
                for line in game_matrix:
                    print(line)
                return
player_1_loop()




#Only have 1 go per player