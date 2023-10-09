# def hello_world(name, age = 21):
#     print(f"Hello, {name}, you are {age} years old!")

# x = "John"
# hello_world(name = input("What is your name? "), age = input("What is your age? "))


def add_gst(num = float(input("Enter the number you want to convert here: ")), shipping = float(input("Enter shipping here: ")), tax_rate = float(input("Enter tax_rate here: "))):
    total = (num * tax_rate) + shipping + num
    print(f"Total = {total:.2f}")



add_gst()

