''' Q2:
Given a python list [10, 501, 22, 37, 100, 999, 87, 351]
your task is to count all Prime Numbers and create a new
list which contains all the Prime Numbers in it? '''

'''
Input = Python List
logic = for loop with if statement and append method for list
Output = print (Prime number list)
'''

# Given Python List
python_list = [10, 501, 22, 37, 100, 999, 87, 351]

# New Empty list for Prime Numbers
prime_numbers = []

# For Loop with if statement to find prime numbers and then append to respective list
for number in python_list:
    if number >1:
        for i in range(2, int(number**0.5) + 1):
           if number % i == 0:
               break
        else:
            prime_numbers.append(number)
    
# Print Prime Number
print("Prime numbers:", prime_numbers)
