#!/usr/bin/env python


# While loops
# While something is true, execute the code in the loop
# while loops wait for a condition to be false to stop
"""
counter = 1
while counter < 100:
    print(counter)
    counter += 4 #short form: counter = counter + 4
    # Watch out: stack overflow error

"""

"""
count2 = 0
while count2 > 1:
    print("This shouldn't print")
"""



"""
# Lists

# lists contain multiple elements
# Index starts at 0

# Adding to lists
list1 = []
list2 = [1, 2, 3]

print(type(list1))

list1.append("Bye")
list1.append("Hi") #add to the end as-is
# append will always add 1 element

print(list1)

#list1.extend(list2)  # like pouring in a basket

list1.append(list2)
print(list1)

list1.insert(1, "boo")
print(list1)

print(len(list1)) #len() tells you the number of elements inside

# Removing from a list

list1.pop(2) # The index
print(list1)

list1.remove('Bye') #looks for an item
print(list1)

del(list1[1][0]) #index in square brackets
print(list1)

list1.clear() #throw everything in the list out
print(list1)
"""





# Lists can contain multiple types of items
"""
a1 = [1, 2.1, "three"]
c
# You can loop through the items in the list
for item in a1:
    print(type(item))
    
# The loop does the same thing as above, but you also get a number for the current index
for i in range(len(a1)):
    print(type(a1[i]))
"""



# Checking if two lists are the same length
"""
A = [1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1]

print(len(A) == len(B))
"""

# How many elements in A are bigger than the corresponding item in B?
"""
count = 0
for i in range(len(A)):
    if A[i] > B[i]:
        count += 1
print(count)
"""


# Remove all items of type str in a list
"""
a1 = [1, 2.1, "three"]

for item in a1:
    print(type(item))
    if type(item) is str:
        a1.remove(item)
print(a1)
"""
