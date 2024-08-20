''' Q9:
You have given a Python list [10, 20, 30, 9] and a value of 59.
Write a Python program to find the triplet in the list whose sum
is equal to the given value. '''

'''
Input = list[10, 20, 30, 9] and value 59
logic = Triplet Function with 3 parameters, for loop with range function and if statement
Output = print (first no-repeating elements in a given list)
'''

# Given List
list = [10, 20, 30, 9]

# Given Value
value = 59

# Length of given list
length = len(list)

# Function with 3 Parameters
def triplet(list, value, length):  

    # Store the first element as list[i]
    for i in range(0, length - 2):

        # Store the second element as list[j]
        for j in range(i + 1, length - 1): 

            # Store the third element as list[k]
            for k in range(j + 1, length):

                # Check the sum of the 3 elements is equal to the given value
                if list[i] + list[j] + list[k] == value:

                    # Print sum of triplet
                    print(f"Triplet is {list[i]}, {list[j]} and {list[k]}")  
                    return True
    return False

# Function Call
triplet(list, value, length)  