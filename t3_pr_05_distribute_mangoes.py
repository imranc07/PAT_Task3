'''Q5:
You have given a list of N integers which represents the number of Mangoes in a bag.
Each bag has a variable number of Mangoes.
There are M students in a Guvi Class.
Your task is to distribute the Mangoes in such a way that
each student gets one bag.
The difference between the number of Mangoes and in a bag with maximum
Mangoes and Bag with minimum Mangoes given to the student is minimum'''

'''
Input:
1. N integers which represents Mangoes in a bag
2. Each bag has a variable number of Mangoes
2. M students in Guvi Class

Logic:
1. List of mangoes
2. Funcntion to distribute number of mangoes
3. Calculate the minimum difference using for loop
4. Allocate bags to students using for loop with range function

Output:
1. Minimum difference
2. Student with minimum mangoes
'''

# List of mangoed
mangoes = [10, 50, 22, 37, 11, 8, 19, 17, 31]

# print(sorted(mangoes))
students = int(input("Enter the number of Students: "))

# Function to distribute mangoes to each student
def distribute_mangoes(mangoes, students):
    
    # Sort the mangoes in ascending order
    mangoes.sort()  
    mangoes_in_bag = len(mangoes)
    
    # Initialize minimum difference
    min_diff = float('inf')

    # Calculate the minimum difference
    for i in range(mangoes_in_bag - students + 1):
        diff = mangoes[i + students - 1] - mangoes[i]
        min_diff = min(min_diff, diff)

    # Allocate bags to students
    allocation = [[] for x in range(students)]
    for i in range(mangoes_in_bag):
        allocation[i % students].append(mangoes[i])

    return allocation, min_diff

result, min_difference = distribute_mangoes(mangoes, students)

# Print the Minimum Difference
print("Minimum Difference:", min_difference)
for i, bags in enumerate(result):

    # Print stundents with number of bags
    print(f"Student {i + 1} gets bags:", bags)  