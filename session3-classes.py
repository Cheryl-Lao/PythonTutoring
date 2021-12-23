#!/usr/bin/env python

scope = "global scope"
# Functions
# Like functions in calculus!
# The things in the brackets are parameters (inputs to your function)

"""
def y_intercept_finder(m, x, b):
    scope = "local scope"
    print(scope)
    return m * x + b

print(scope)
intercept = y_intercept_finder(1, 2, 3) # saved return
print(y_intercept_finder(3, 6, 5))
"""


"""
lst = [8, 9, 0]
# functions don't have to have a return value
# !! functions are like units of instructions
def list_doubler(lst):
    for i in range(len(lst)):
        lst[i] *= 2


sample_list = [1, 2, 3]
list_doubler(sample_list)
list_doubler(sample_list)
print(list_doubler(lst)) # There was no return -- None
print(lst)
print(sample_list)
"""


"""
# -- Debugging --
# Click left side of the line to make a breakpoint
# Click little bug next to play button for debug mode
def is_even(num):
    return num % 2 == 0

# put breakpoints where there's something suspicious
for i in range(5):
    print("hi")
    print("hi again")
    if is_even(i):
        print(str(i) + " is even")
    else:
        print(str(i) + " is odd")
"""




# Classes are like types
# They are used to organize objects in object-oriented programming

class Book:
    # A simple example Book class

    # initialization

    def __init__(self, title, author, pages): # Constructor
        # Attributes
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return self.title + " by " + self.author + ". " + str(self.pages) + " pages long"

CherylsBook = Book("The Old Man and the Sea", "Ernest Hemingway", 127)
CahvinsBook = Book("Titanic", "Celine Dion", 125)

Bookshelf = [CherylsBook, CahvinsBook]
print(CherylsBook.title)
print(CahvinsBook.title)


print(CherylsBook)
print(Bookshelf)


# -- Practice Problems --

# Write a function that calculates the number of seconds when given the number of hours as a parameter
"""
def hours_to_seconds(hours):
    return hours * 60 * 60

print(hours_to_seconds(1))
"""

# Create two lists of Book objects. Compare the titles in the lists of books to see if there are any duplicate titles between the bookshelves. Print the title if there's a duplicate
"""
Book1 = Book("The Old Man and the Sea", "Ernest Hemingway", 127)
Book2 = Book("Titanic", "Celine Dion", 125)
Book3 = Book("Cracking the Coding Interview", "Gayle Laakmann McDowell", 706)
Book4 = Book("To Kill a Mockingbird", "Harper Lee", 201)
Book5 = Book("The Old Man and the Sea", "Ernest Hemingway", 127)
Book6 = Book("Cracking the Coding Interview", "Gayle Laakmann McDowell", 706)

Bookshelf1 = [Book1, Book2, Book3]
Bookshelf2 = [Book4, Book5, Book6]

print("Duplicates: ")
for i in range(len(Bookshelf1)):
    for j in range(len(Bookshelf2)):
        if Bookshelf1[i].title == Bookshelf2[j].title:
            print(Bookshelf1[i].title)
"""




# Add an attribute called in_library to the Book class
# solution: Change the __init__ function to look like this instead:
"""
def __init__(self, title, author, pages, in_library): 
    # Attributes
    self.title = title
    self.author = author
    self.pages = pages
    self.in_library = in_library
"""
