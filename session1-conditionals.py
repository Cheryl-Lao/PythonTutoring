#!/usr/bin/env python

#Checking types
"""
thing1 = 100.0
print(type(thing1)) # <class 'float'>

print(isinstance(thing1, float)) #true/false
"""

"""
print(type("This string"))
print(isinstance(100, (int, str)))
"""



# Booleans made of comparators
# ==
# >, <, or >=, <=
"""
true_false = 1 >= 2
print(true_false)
print(type(true_false))

true_false = "cuashbthf"
print(true_false)
print(type(true_false))
"""

"""
bool1 = 1 == 1
bool2 = 1 == 2
bool3 = 1 < 2
bool4 = "thing" == 1
"""


# Negation
"""
print(not isinstance(100, (int, str)))
"""


"""
print(not 1 == 2)
print(1 != 2)

"""


# if statements
"""
weather = "rainy"
mood = "happy"
if weather == "rainy" and mood == "happy":
    print("rainboots")
elif weather == "sunny":
    print("sandals")
elif weather == "cloudy":
    print("sneakers")
else:
    print("any shoes")
"""




"""
if bool1:
    print("First case")

if bool2:
    print("Second Case")

# if-else statements
if True:
    print("Third Case")
elif True:
    print("Fourth Case")
else:
    print("Fifth Case")
"""

# Match-case statements (New in python 3.10)
# switch statements
"""
x = 'c'
match x:
    case 'a':
        print("thing")
    case 'b':
        print("other thing")
    case _:
        print("last thing")
"""
#TODO try to write if-statement version of this

# for loops
#for i in range(4,7):
#    print(i)

#TODO try other nested for loops
for i in range(10): # 0 to 9
    #if i % 2 == 0: # % modulo : gives you the remainder
    #    print(i)
    #print("hi")
    for j in range(10):  # 0 to 9
        # if i % 2 == 0: # % modulo : gives you the remainder
        #    print(i)
        print(str(i) + " " +str(j))
print("bye")



"""
for i in range(7):
    print(i)


for i in range(10):
    if i % 2 == 0:
        print(i)
"""