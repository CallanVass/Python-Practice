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




# Original list
arr = [5, 22, 29, 39, 19, 51, 78, 96, 84]
# Declaring variable for iteration
i = 0
# While loop using the len() function to determine if i is less than the last value
while i < len(arr) - 1:
    #If i is i is greater than the next value
    if arr[i] > arr[i + 1]:
        #Decalring placeholder value to store i for later use
        place_holder = arr[i]
        #Swapping i with the value to the right (i + 1)
        arr[i] = arr[i + 1]
        #Taking the swapped value and placing it where i used to be
        arr[i + 1] = place_holder
        #Print which numbers are swapping, along with the element's position
        print(f"Swapping {arr[i]} (element number {i}) with {arr[i + 1]}")
        #Printing array for reference
        print(arr)
        #Returning to the first element to check if there are more elements to swap
        i = 0
    #If the if statement doesn't meet it's conditions, add one to i (to continue iteration)
    else: 
        i += 1


