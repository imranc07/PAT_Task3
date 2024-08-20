'''Q1:
You have given a python list [10, 501, 22, 37, 100, 999, 87, 351]
your task is to create a two list one which have all the Even
numbers and another list which will have all the Odd numbers in it? '''

'''
Input = Python List
logic = for loop with if statement and append method for list
Output = print (Even and Odd number list)
'''

# Given Python List
python_list = [10, 501, 22, 37, 100, 999, 87, 351]

# New Empty list for Even Numbers
even_numbers = []

# New Empty List for Odd Numbers
odd_numbers = []

# For Loop with if statement to find even and odd number and then append to respective list
for number in python_list:
    if number % 2 == 0:
        even_numbers.append(number)
    else:
        odd_numbers.append(number)

# Print Even Nuumber
print("Even numbers:", even_numbers)

#Print Odd Number
print("Odd numbers:", odd_numbers)