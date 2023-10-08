# arr = [5, 22, 29, 39, 19, 51, 78, 96, 84]
# i = 0
# while (i<arr.len( -1) and (arr[i] < arr[i+1])):
#     i += i
#     print(i)
#     arr[i] = arr[i+1]
#     arr[i + 1] = arr[i]

# arr = [5, 22, 29, 39, 19, 51, 78, 96, 84]
# i = 0
# while (i < len(arr) -1) and (arr[i] < arr[i+1]):
#     i += i
#     print(i)
#     arr[i] = arr[i+1]
#     arr[i + 1] = arr[i]
#     print(arr)

# arr = [5, 22, 29, 39, 19, 51, 78, 96, 84]
# i = 0
# while i < len(arr)-1 and (arr[i] < arr[i+1]):
#     print(i)
#     arr[i], arr[i + 1] = arr[i + 1], arr[i]
#     print(arr)
#     i += 1

# arr = [5, 22, 29, 39, 19, 51, 78, 96, 84]
# i = 0
# while (i < (len(arr) - 1) and (arr[i] < arr[i + 1])):
#     i += 1
#     print(i)
#     arr[i] = arr[i+1]
#     arr[i + 1] = arr[i]
#     print(arr)

#COMPLETED CODE SNIPPET TO ORGANISE AN UNORGANISE LIST INTO ASCENDING ORDER


# # Original list
# arr = [5, 22, 29, 39, 19, 51, 78, 96, 84]
# # Declaring variable for iteration
# i = 0
# # While loop using the len() function to determine if i is less than the last value
# while i < len(arr) - 1:
#     #If i is i is greater than the next value
#     if arr[i] > arr[i + 1]:
#         #Declaring placeholder value to store i for later use
#         place_holder = arr[i]
#         #Swapping i with the value to the right (i + 1)
#         arr[i] = arr[i + 1]
#         #Taking the swapped value and placing it where i used to be
#         arr[i + 1] = place_holder
#         #Print which numbers are swapping, along with the element's position
#         print(f"Swapping {arr[i]} (element number {i}) with {arr[i + 1]}")
#         #Printing array for reference
#         print(arr)
#         #Returning to the first element to check if there are more elements to swap
#         i = 0
#     #If the if statement doesn't meet it's conditions, add one to i (to continue iteration)
#     else: 
#         i += 1


#WEATHER CHALLENGE


# def weather_function(rain, temp):
#     if rain:
#         if temp < 15:
#             return "It's wet and cold"
#         else:
#             return"It's warm and raining"
#     else:
#         if temp < 15:
#             return "It's not raining but cold"
#         else:
#             return "It's warm but not raining"
        
# print(weather_function(True, 14))



# ACME CORP CHALLENGES

coding_dict = {
    "python": 1,
    "ruby": 2,
    "bash": 4,
    "git": 8,
    "html": 16,
    "tdd": 32,
    "css": 64,
    "javascript": 128

}
coding_list = ("")

#enter coding languages, plus them together

print("Python, Ruby, Bash, Git, HTML, TDD, CSS, Javascript")
coding_score = input("From the list above, and seperated by only a space, please enter which languages you're proficient in: ")
coding_list = coding_score.split()
print("You chose: ", coding_list)
i = 0
while i < len(coding_list) -1:




