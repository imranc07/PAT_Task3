''' Q8:
Write a python program to find the minimum element in a rated and sorted list. '''

'''
Input = List
logic = Function to calculate minimum element, for loop with if statement
Output = print (first no-repeating elements in a given list)
'''


# Input List
list = [10, 50, 22, 37, 10, 18, 9, 7, 31]  

# Print the input list
print("Input List =", list)  

# Define a function
def min_element(list):

    #  Initialize a variable x_min with value as first element of list
    x_min = list[0]  
    
    # Iterates through all the elements in the list
    for i in range(len(list)):
    
        # Compare the current element with x_min
        if list[i] < x_min:
    
            # If the current element is less than x_min, replace the current element as x_min
            x_min = list[i]  
    return x_min

# Print minimum element list
print("Minimum element is", min_element(list))