''' Q10:
Given a list [4, 2, -3, 1, 6]. Write a python program to 
find if there is a sub list with sum equal to Zero? '''

'''
Input = list[4,2,-3,1,6] and value 0
logic = Function to calculate sub list with sum = 0, for loop with range() and if statement, append method
Output = print (Sub List wth sum equal to zero)
'''

# Given List
list = [4,2,-3,1,6]

# Given Value
value = 0

# Length of Input list
length = len(list)

# Define a function with 3 parameters
def sub_list(list, value, length):

    # New emprt list  
    new_list = []

    # Store the first element as list[i]
    for i in range(0, length):

        # Store the second element as list[j]
        for j in range(i + 1, length):  

            # Store the third element as list[k]
            for k in range(i + 2, length):  

                # Check the sum of the 3 elements is equal to the given value
                if list[i] + list[j] + list[k] == value:  
                    new_list.append((list[i], list[j], list[k]))
    return new_list

# Function Call 
new_list = sub_list(list, value, length)

# Print sublist with sum equal to zero
print("Sub List wth sum equal to zero:",new_list)