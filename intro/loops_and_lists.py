# spam = 0

# while spam < 5:
#     spam += 1
#     print("Hello")
#     print(spam)

# print("Done")



# for spam in range(5):
#     print(f"Hi!  {spam}")

# print("done")



# import random

# count = int(input("How many integers do you want? "))

# for i in range(count):
#     print(random.randint(1, 100))

#todo: assignment go and create another elif case at the bottom where you reference nothing in thee
#languages and output needing to have a value (error message)



spam = ["cat", "dog", "cat", "cat", "red"]
num = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]

spam[0] = "MEOW"
# index = 1
for index, num in enumerate(spam):
    print(f" {index + 1}. {num}")
    # index += 1