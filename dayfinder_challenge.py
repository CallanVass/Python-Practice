def dayFinder():
    day = input("Enter which day it is: ")
    
    if day == "Wednesday" or day == "wednesday":
        print("It's Wednesday!")
    
    day = input("What day is it? ")
    if not day.endswith("y"):
        print("That's not a day, champion!")
    elif day == "Wednesday" or day == "wednesday":
        print("Haha, you're a funny one! See ya!")
    else:
        print("Thank you for letting me know that today is " + day + "! See ya!")
    return

dayFinder()