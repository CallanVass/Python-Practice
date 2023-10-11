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

#COMPLETED CODE SNIPPET TO ORGANISE AN UNORGANISE LIST INTO ASCENDING ORDER (which turned out to be not what they wanted. Code rewrote below to do exactly as asked)


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


#Rewritten code

# arr = [5, 22, 29, 39, 19, 51, 78, 96, 84]

# i = 0

# while i < len(arr) - 1:

#     if arr[i] > arr[i + 1]:
#         place_holder = arr[i]
#         arr[i] = arr[i + 1]
#         arr[i + 1] = place_holder
#         print(arr)
#         break
#     else:
#         i += 1
    

# arr = [5, 22, 29, 39, 19, 51, 78, 96, 84]

# i = 0

# while i < len(arr) - 1:

#     if arr[i] > arr[i + 1]:
#         place_holder = arr[i]
#         arr[i] = arr[i + 1]
#         arr[i + 1] = place_holder
#         print(arr)
#         break
#     else:
#         i += 1


# arr = [5, 22, 29, 39, 19, 51, 78, 96, 84]
# i = 0
# while (i < len(arr) -1):
#     i += 1 
#     if arr[i] > arr[i+1]:
#         temp = arr[i]
#         arr[i] = arr[i+1]
#         arr[i + 1] = temp
#         print(arr)
#         break
     



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

# def coding_names():
#     python = 1
#     ruby = 2
#     bash = 4
#     git = 8
#     html = 16


# coding_dict = {
#     "python": 1,
#     "ruby": 2,
#     "bash": 4,
#     "git": 8,
#     "html": 16,
#     "tdd": 32,
#     "css": 64,
#     "javascript": 128

# }
# coding_list = ("")


# all_p_languages = ["Python", "Ruby", "Bash", "Git", "HTML", "TDD", "CSS", "Javascript"]
# print("Python, Ruby, Bash, Git, HTML, TDD, CSS, Javascript")
# coding_score = input("From the list above, and separated by only a space, please enter which languages you're proficient in: ")
# coding_list = coding_score.split()
# print("You chose: ", coding_list)
    
# new_coding_list = 0

# for p_language in coding_list:
#     if p_language.lower() == "python":
#         new_coding_list += 1
#     elif p_language.lower() == "ruby":
#         new_coding_list += 2
#     elif p_language.lower() == "bash":
#         new_coding_list += 4
#     elif p_language.lower() == "git":
#         new_coding_list += 8
#     elif p_language.lower() == "html":
#         new_coding_list += 16
#     elif p_language.lower() == "tdd":
#         new_coding_list += 32
#     elif p_language.lower() == "css":
#         new_coding_list += 64
#     elif p_language.lower() == "javascript":
#         new_coding_list += 128


# print(f"You're total coding score is: {new_coding_list}!")

# all_p_languages = [lang.lower() for lang in all_p_languages]

# all_p_languages = [lang for lang in all_p_languages if lang not in coding_list]

# all_p_languages = [lang.capitalize() for lang in all_p_languages]


# language_scores = {
#     "Python": 'Python: 1 point',
#     "Ruby": "Ruby: 2 points",
#     "Bash": "Bash: 4 points",
#     "Git": "Git: 8 points",
#     "Html": "HTML: 16 points",
#     "Tdd": "TDD: 32 points",
#     "Css": "CSS: 64 points",
#     "Javascript": "JavaScript: 128 points"
# }

# def assign_scores(languages):
#     scores = []
#     for lang in languages:
#         if lang in language_scores:
#             scores.append(language_scores[lang])
#     return scores

# if not assign_scores(all_p_languages):
#     print("You're perfect!")
# else:
#     print(f"You may want to learn about: {assign_scores(all_p_languages)}")
  




# def sum_to_one_hundred():
#     result = 1
#     for num in range(101):
#         result += num
#         print(f"{num + 1}: {result}")
#     return result


# print(sum_to_one_hundred())



prime_list = []
for i in range(2, 101):
    prime = True
    for x in range(2, i):
        if (i % x) == 0:
            prime = False
            break
    if prime:
        prime_list.append(i)



print(prime_list)
            
#CREATE prime_list
#FOR loop (i) within range of 2 to 101
#IF for loop is still within it's range, CREATE prime = True
#Nested FOR loop (x) to check if the number given by the previous loop meets conditions for new IF statement (below)
#IF statement to see if (x) is divisible by anything other than (i) and 1
#If IF statement is found to be true, then prime = False and break from the line
#IF statement linked to (x) loop. IF prime = True, append the number to prime_list



