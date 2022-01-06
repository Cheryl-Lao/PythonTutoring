# -- Recursion --
"""
Recursion is a way of decomposing a problem down to simpler parts:
The base case(s) and the recurrence relation

"""
"""
def fibonacci(n):
    if n == 0: # Base Case
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2) # Recurrence Relation

print(str(fibonacci(1)) + " +  " + str(fibonacci(2)))
print(fibonacci(3))

"""




# Pascal's triangle
# f(i, j) = f(i-1, j-1) + f(i-1, j)  ith row and jth column
# f(i, j) = 1 when j = 1 or j = i

"""
def pascalsTriangle(i, j): # i = row number    and j = item number in column
    if j == 1 or j == i: #base case
        return 1
    return pascalsTriangle(i-1, j-1) + pascalsTriangle(i-1, j) #recurrence relation

print(pascalsTriangle(3, 3))
"""


# -- Dictionaries --
"""
# Keys are unique
# Also known as hashmaps in other languages
my_dictionary = {"A": ["Apple", "air"], "B": ["ball", "blue", "balloon"]}
my_dictionary["C"] = ["car", "circle"]
print(my_dictionary)
#JSON is an example of this
#https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON

"""



# -- Sets --
# checking if an element exists in a set is faster than in a list
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Sets don't have a specific order
other_set = {5, 4, 3, 2, 1}
print(my_set == other_set)

# You can also make a set from a list
my_set = set([1, 2, 3, 4, 5])

my_set.add(5)
print(my_set)



# -- Practice Problem --
# Practice: Write a recursive function that finds the harmonic sum of a number n
def harmonic_sum(n):
  if n <= 1: # Base case
    return 1
  else:
    return 1 / n + (harmonic_sum(n - 1)) #Break the problem down into 1/n plus the simpler problems

print(harmonic_sum(7))

# Practice: Create a dictionary that counts how many times each item appears in a list
fruit_inventory = ["apple", "orange", "apple", "pear", "peach", "plum", "pear", "pear", "peach"]
def list_to_occurences(lst):
    new_dict = {}
    for item in lst:
        if item in new_dict:
            new_dict[item] += 1
        else:
            new_dict[item] = 1
    return new_dict

print(list_to_occurences(fruit_inventory))

# Practice 2D arrays:
# Write a function that returns a list consisting of the i-th item of each list in a 2D list
practice_array = [[1],
                  [2, 3, 4],
                  [5, 6],
                  [7, 8, 9, 10]]

def ith_items(lst, i):
    items = []
    for subarray in lst:
        if len(subarray) >= i:
            items.append(subarray[i])
    return items

print(ith_items(practice_array, 0))

# -- List comprehensions --
"""
# List comprehensions are shorthand ways of creating lists (replaces the loop that you would otherwise have to write to create it)

newlist = []

for num in range(1, 11):
  if num % 2 == 0:
    newlist.append(str(num))

print(newlist)

# That loop is the same as:
anotherList = [str(num) for num in range(1, 11) if num % 2 == 0]
# The items in the list are x for each fruit called x in the fruits list. The condition is that the fruit x needs to have "a" in its name

print(anotherList)
"""

