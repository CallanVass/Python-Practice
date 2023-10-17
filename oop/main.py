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


# game_matrix = [[" ", " ", " "],
#                 [" ", " ", " "],
#                 [" ", " ", " "]]

# winning_dict = {
#     "Player_1_wins": 0,
#     "Player_2_wins": 0
# }

# print("Welcome to TICK TACK TOE!")
# player_1 = input("Please enter the name of the first Player: ")
# player_2 = input("Please enter the second Player: ")

# player_1_mark = "X"
# player_2_mark = "O"



# print(f"{player_1} will be going first! They are 'X'")




def check_winner(board, player):
    pass
    #Check for the conditions of the winner

def check_draw(board):
    pass
    #Check for the conditions of a draw

def get_player_move():
    pass
    #Get player input for move
def tic_tac_toe_game():
    pass




def display_board(board):
    for col in board:
        print(" | ".join(col))
        print("-" * 9)
        if col == board[2]:
            break




game_board = [[" ", " ", " "],
             [" ", " ", " "],
             [" ", " ", " "]]

display_board(game_board)