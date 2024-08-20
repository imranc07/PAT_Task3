''' Q4:
Write a python program to find the sum of first and last digit on an integer.'''

'''
Input = User entered integer
logic = def function  with arguments, type casting, return values
Output = print (Even and Odd number list)
'''


# Take user input
number = int(input("Enter an integer: "))

def sum_first_last_digit(number):

    # Convert the number to a string to access its digits
    num_str = str(number)
    
    # Get the first digit 
    first_digit = int(num_str[0])
    
    # Get the last digit
    last_digit = int(num_str[-1])
    
    # Calculate the sum of the first and last digit
    return first_digit + last_digit

result = sum_first_last_digit(number)
    
# Print the sum of first and last digit of integer
print(f"Sum of the first and last digit of the integer is {result}")
