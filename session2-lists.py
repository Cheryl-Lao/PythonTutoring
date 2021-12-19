# lists

#lists contain multiple elements
#Adding to lists
list1 = []
list2 = [1, 2, 3]
list1.append("Hi")
list1.extend(list2)
list1.insert(1, "boo")

#Removing from a list
list1.pop(0)
list1.remove(2)
del(list1[3])
list1.clear()




#lists can contain multiple types of items
"""
a1 = [1, 2.1, "three"]

for item in a1:
    print(type(item))
    if type(item) is str:
        print("item is a string")
"""


#Checking if two lists are the same length
"""
A = [1, 2, 3, 4, 5]
B = [5, 4, 3, 2, 1]

print(len(A) == len(B))
"""

#How many elements in A are bigger than the corresponding item in B?
"""
count = 0
for i in range(len(A)):
    if A[i] > B[i]:
        count += 1
print(count)
"""


#remove all items of type str in a list
"""
a1 = [1, 2.1, "three"]

for item in a1:
    print(type(item))
    if type(item) is str:
        a1.remove(item)
print(a1)
"""
