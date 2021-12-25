#!/usr/bin/env python

class Book:
    # A simple example Book class

    # initialization
    def __init__(self, title, author, pages): # Constructor
        # Attributes
        self.title = title
        self.author = author
        self.pages = pages

    # toString() method
    # Tells the program how to format a string version of this object nicely
    def __str__(self):
        return self.title + " by " + self.author + ". " + str(self.pages) + " pages long"

    # Equals method
    # Tells the program what conditions makes two of these objects equal
    def __eq__(self, other_book):
        return self.title == other_book.title


class Bookshelf:
    def __init__(self, books=[]): # Constructor with a default value for the book list
        # The books list is empty if it's not specified
        self.books = books

    # This is an example of a method -- a function that only works for a member of a certain class
    def shelve_book(self, book):
        # Check if the item is actually a book before shelving it
        if isinstance(book, Book): # (input, type)
            self.books.append(book)
        else:
            print("Cannot shelve something that is not a book")


# ebook extends Book
class eBook(Book):
    def __init__(self, title, author, pages, platform):
        super().__init__(title, author, pages) #Calls the superclass __init__
        self.platform = platform


myBook = Book("The Old Man and the Sea", "Ernest Hemingway", 127)

myBook2 = Book("The Old Man and the Sea", "Ernest Hemingway", 127)

#print(myBook)
#print(myBook.__str__())
#print(myBook == myBook2)
#print(myBook.__eq__(myBook2)) #the same as above
#print(myBook.title) # use . to access attributes

myeBook = eBook("The Old Man and the Sea", "Ernest Hemingway", 127, "Kindle")

print(myeBook.platform)
#print(myBook.platform) #doesn't work

myBookshelf = Bookshelf()

myBookshelf2 = Bookshelf()

myBookshelf.shelve_book(myBook)
print(myBookshelf)

#print([str(book) for book in myBookshelf.books]) #list comprehension -- We can go over this next time

#print(myBookshelf.books[0].title)



# Practice Problems:

# Add a new audiobook subclass that has a new attribute called "recording_length" and a new method called "play()" that just prints "Playing: " and then the book name
class audioBook(Book):
    def __init__(self, title, author, pages, recording_length):
        super().__init__(title, author, pages) #Calls the superclass __init__
        self.recording_length = recording_length

    def play(self):
        print("Playing: " + self.title)


# Add a new __str__ method to the Bookshelf class that formats a bookshelf list nicely
    #def __str__(self):
    #    str_version = ""
    #    for book in self.books:
    #        str_version = str_version + book.title + ", "
    #    return str_version