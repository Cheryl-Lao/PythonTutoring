#!/usr/bin/env python

# -- String Splicing --
string_to_splice = "0123456789"
print(string_to_splice[1:3])
print(string_to_splice[:3])
print(string_to_splice[1:])

# going backwards with the range function
for num in range(10, 2, -2):
    print(num)

# -- 2D arrays --
class tictactoe_board():
    def __init__(self):
        self.board = [["-", "-", "-"], ["-", "-", "-"], ["-", "-", "-"]]

    # Plays a certain character to the given location
    def playPosition(self, character,  i, j):
        self.board[i][j] = character
    def __str__(self):
        board_str = ""
        for row in self.board:
            for item in row:
                board_str += item
            board_str += "\n"

        return board_str


ttb = tictactoe_board()
#print(ttb)
ttb.playPosition("X", 0, 0)
ttb.playPosition("O", 0, 1)
ttb.playPosition("X", 0, 2)
ttb.playPosition("O", 1, 0)
ttb.playPosition("X", 1, 1)
ttb.playPosition("O", 1, 2)
ttb.playPosition("X", 2, 0)
ttb.playPosition("X", 2, 1)
ttb.playPosition("O", 2, 2)

print(ttb)


# -- Recursion --
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


# TODO Practice problem: Write a function that checks if X or O won on a board. Take the character in as a parameter and return true or false
"""
    def checkWin(self, character):
    # Three cases for wins:

    # 1) Win across a row
    row_win = False # Start by assuming that you don't have a win on the board
    for row in self.board:
        single_row_win = True # Assume that you have a win in this particular row until you find otherwise
        for i in range(len(row)):
            if row[i] != character:
                single_row_win = False # If any of the characters in the row don't match, they've lost
        row_win = row_win or single_row_win # a single True in any of the rows will make this True

    # Win across a column
    column_win = False
    for i in range(len(self.board[0])): # This is very similar to the row win code, except we're looping over the board column-by-column
        single_column_win = True
        for row in self.board:
            if row[i] != character:
                single_column_win = False
        column_win = column_win or single_column_win

    # Win across the major diagonal (top left to bottom right)
    major_diag_win = True
    for i in range(len(self.board)):
        if self.board[i][i] != character: # The major diagonal is where the row and column coordinates are equal
            major_diag_win = False

    # Win across the minor diagonal
    minor_diag_win = True
    for i in range(len(self.board)):
        if self.board[i][len(self.board) - 1 - i] != character: # The minor diagonal is where the column number is equal to the width of the board minus the current row number - 1
            minor_diag_win = False

    return row_win or column_win or major_diag_win or minor_diag_win

print(ttb.checkWin("X"))
"""



