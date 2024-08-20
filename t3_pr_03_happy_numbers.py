''' Q3:
Given a python list [10, 501, 22, 37, 100, 999, 87, 351]
Find out how many numbers are there in the given Python list
which are Happy Numbers? '''


'''
Defination of Happy Number:
A number is said to be happy if it yields 1 when replaced by the sum of squares of its digits repeatedly.
If this process results in an endless cycle of numbers containing 4, then the number will be an unhappy 
number.

Let's understand by an example:

Number = 32
3^2 + 2^2 = 13
1^2 + 3^2 = 10
1^2 + 0^2 = 1
'''

'''
Input = Python List
logic = Happy number function with def keyword and arguments, while loop, membership & comparison operators 
Output = print (Happy number count and list)
'''

# Given Python List
python_list = [10, 501, 22, 37, 100, 999, 87, 351]

# A function to get Happy Numbers
def happy_num(num):

    # Empty list to store the happy numbers
    Happy_Numbers = []  

    #Loop for to check Happy Number
    while num != 1 and num not in Happy_Numbers:

        # Append the Happy Numbers to the Happy_Numbers list
        Happy_Numbers.append(num)  
        num = sum(int(digit) ** 2 for digit in str(num))

    # If num equals 1, then it's a happy number
    return num == 1  

# Check whether it is a happy number using happy_num(num)
Happy_Numbers = [num for num in python_list if happy_num(num)]  

# A Function to count number of Happy_Numbers
def count_happy_numbers(python_list):
    # Initialize count as 0
    count = 0
    
    # Iterate through each number in the list
    for num in python_list:
        
        # Check if the number is happy using is_happy function
        if happy_num(num):
        
            # increment the counter
            count += 1
    
    # Return the count of happy numbers
    return count

# Count happy numbers
happy_count = count_happy_numbers(python_list)

# Print the Given Python List
print("Given Python List =", python_list) 

# Print the count of happy numbers
print("Number of happy numbers in the list:", happy_count)

# Print Happy Number List
print("Happy Numbers =", Happy_Numbers)  