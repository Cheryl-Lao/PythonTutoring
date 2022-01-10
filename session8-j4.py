"""
# number of each letter
num_l = 0
num_m = 0
num_s = 0

lost_l = 0
lost_m = 0

m_in_l = 0
l_in_m = 0
#MLLMS
#MLLSM

# input
books = input() #string

# LLMS
# count # of books
for i in range(len(books)):
    if books[i] == "L":
        num_l += 1
    elif books[i] == "M":
        num_m += 1
    elif books[i] == "S":
        num_s += 1


# Go through the L section
for i in range(0, num_l):
    if books[i] == "M":
        lost_l += 1
        m_in_l += 1
    elif books[i] == "S":
        lost_l += 1

# Go through the M section
for i in range(num_l, num_l + num_m):
    if books[i] == "L":
        lost_m += 1
        l_in_m += 1
    elif books[i] == "S":
        lost_m += 1

answer = lost_l + lost_m - min(m_in_l, l_in_m)
print(answer)
"""


# Look through a list of numbers and find all the elements that are greater than its index number. Return the number of items that are greater than the indices where they’re found

"""
my_list = [0, 4, 2, 3, 7, 5, 6]

def index_counter(lst):
    count = 0
    for i in range(len(lst)):
        if lst[i] > i:
            count += 1
    return count
print(index_counter(my_list))

"""

# Write a function that looks through a nested list for a certain number
# Hint: it involved recursion and you need to use isinstance(SOMETHING, list)
"""
example = [[1, 2], 3, [[4, [5]]]]

def recursive_find(lst, num):
    found = False
    for item in lst:
        if isinstance(item, list):
            found = found or recursive_find(item, num)
        else:
            found = item == num
    return found

print(recursive_find(example, 5))
"""
