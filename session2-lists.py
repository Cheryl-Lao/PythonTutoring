#!/usr/bin/env python
# Lists

# lists contain multiple elements
# Index starts at 0

# Adding to lists
"""
list1 = []
list2 = [1, 2, 3]

list1.append("Hi")
print(list1)

list1.extend(list2)
print(list1)

list1.insert(1, "boo")
print(list1)
"""

# Removing from a list
"""
list1.pop(0)
print(list1)

list1.remove(3)
print(list1)

del(list1[0])
print(list1)

list1.clear()
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
