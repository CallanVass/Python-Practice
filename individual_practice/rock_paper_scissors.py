
# def displayResult(choice):
#     if choice == "r":
#         print("Rock blunts scissors")
#     elif choice == "p":
#         print("Paper wraps rock")
#     else:
#         print("Scissors cuts paper")
#     return






# p1Choice = "r"
# p2Choice = "p"

# if p1Choice == p2Choice:
#     print("It's a draw!")
# elif 








# CODE TO COPY
# BEGIN DisplayResult(choice)
#   if choice = r
#     Output "Rock blunts scissors"
#   else if choice = p
#     Output "Paper wraps rock"
#   else
#     Output "Scissors cuts paper"
#   end
# END

# If p1Choice = p2Choice then
#   Output "Draw"
# Else If (p1Choice = r and p2Choice = s) OR (p1Choice = p and p2Choice = r) OR (p1Choice = s and p2Choice = p) then
#   CALL DisplayResult(p1Choice)
#   Output "player 1 wins"
# Else
#   CALL DisplayResult(p2Choice)
#   Output "player 2 wins" 
# End

# celsius = int(input())

# farenheit = (celsius * 9 // 5) + 32

# print(f"The result is: {farenheit}")


# bank_card_list = bank_card.split()
# bank_card.replace("", " ")
# yes_or_no = input("Y/N? ")
# if yes_or_no == "Y" or "y":
#     pass
# else:
# bank_card_list = bank_card.split()

bank_card = input("Please enter your credit card number here: ")

if bank_card[0] == "4" and len(bank_card) in range(13, 17):
    print("Your bank number is: " + bank_card[1:5])
    print("Your account number is " + bank_card[5:-1])
else:
    print(len(bank_card))
    print("This is not a valid Visa card number.")


