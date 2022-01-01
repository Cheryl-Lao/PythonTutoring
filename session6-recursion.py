# -- Recursion --
"""
Recursion is

"""
"""
def fibonacci(n):
    if n == 0: # Base Case
        return 0
    if n == 1:
        return 1
    return fibonacci(n-1) + fibonacci(n-2) # Recurrence Relation


print(fibonacci(9))
"""



# Pascal's triangle
# f(i, j) = f(i-1, j-1) + f(i-1, j)  ith row and jth column
# f(i, j) = 1 when j = 1 or j = i

"""
def pascalsTriangle(i, j):
    if j == 1 or j == i:
        return 1
    return pascalsTriangle(i-1, j-1) + pascalsTriangle(i-1, j)

print(pascalsTriangle(4, 2))
"""


# -- Dictionaries --
"""
# Also known as hashmaps in other languages
my_dictionary = {}
my_dictionary["key"] = "value"
print(my_dictionary)
#JSON is an example of this
#https://developer.mozilla.org/en-US/docs/Learn/JavaScript/Objects/JSON
"""


# -- Sets --
"""
my_set = {1, 2, 3, 4, 5}
print(my_set)

# Sets don't have a specific order
other_set = {5, 4, 3, 2, 1}
print(my_set == other_set)

# You can also make a set from a list
my_set = set([1, 2, 3, 4, 5])
print(my_set)
"""


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

