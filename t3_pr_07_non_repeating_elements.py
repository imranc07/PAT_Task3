''' Q7:
Write a program to find the first no-repeating elements in a given list of integers '''

'''
Input = List
logic = For loop, remove and append function
Output = print (first no-repeating elements in a given list)
'''

# Input List
list = [84, 28, 84, 33, 86, 28, 86, 54, 23, 33]  

# Empty list to store Repeating elements
Repeat_List = []

# Empty list to store Non-Repeating elements
Non_Repeat_List = []

# For loop toiIterats through each x in list
for x in list:

    # Check if the current element is in Repeat_list
    if x in Repeat_List:
        continue
    
    # Check if the current element is in Non_Repeat_list.
    if x in Non_Repeat_List: 

        # Remove the element from the Non_Repeat_List
        Non_Repeat_List.remove(x)  
        
        # Add that element to the Repeat_List
        Repeat_List.append(x)  
    else:

        # If the current element is not in either list, add it to the Non_Repeat_List
        Non_Repeat_List.append(x) 

# Non-Repeated Elements in List
print("Non-Repeated Elements in List:", Non_Repeat_List)