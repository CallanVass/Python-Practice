#Import math module

import math

#Determine the price of the item the user wishes to buy
item_price = int(input("How much is the item you wish to buy? "))

#Determine user's leftover pay after expenses
pay_after_expenses = int(input("How much is your total weekly pay after expenses? "))

#Divide the price of the item by the amount of pay they entered. The math.ceil function rounds the weeks up
weeks = math.ceil(item_price / pay_after_expenses)

#The f stands for format, and allows the weeks to be added without being turned into strings
print(f"It will take {weeks} weeks for you to save up")