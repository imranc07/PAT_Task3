'''Q6:
You have given three lists. Your task is to find the duplicates in the three lists.
Write a python program for the same. You can use your own python list.'''

'''
Input = 3 List
logic = convert list into set and vice versa, intersection formula
Output = print (dupliates in 3 list)
'''

# Input list1, List2 and List3
list1 = [1, 2, 3, 4, 5, 6] 
list2 = [6, 4, 5, 3, 2, 1] 
list3 = [1, 3, 5, 7, 6, 9] 

# Convert list to set
set1 = set(list1)  
set2 = set(list2)  
set3 = set(list3)

# Find the common numbers in 3 sets
Intersection = set1.intersection(set2).intersection(set3) 

# Convert the set to List
List = list(Intersection)

# Print the duplicates in three lists
print("Duplicates in three lists:", List) 