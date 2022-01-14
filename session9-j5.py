# Based on code from Charles Chen

# Input
rows = int(input())
cols = int(input())
num_lines = int(input())

row_swipes = [False] * rows
col_swipes = [False] * cols

#[False, False, False]
#False = black tile

# R 1
# C 2

#["R", "1"]
#[False, True, False]
for i in range(num_lines): #num_lines = K
    line_info = input().split(" ") # input and split into a list ["R", "1"]
    index = int(line_info[1]) - 1 #row/col number convert to int # Subtract 1 to make it 0-based
    if line_info[0] == "R":
        row_swipes[index] = not row_swipes[index]
    else: # "C" option
        col_swipes[index] = not col_swipes[index]

# Initialize canvas
canvas = [[False for j in range(cols)] for i in range(rows)]

#canvas = []
#for i in range(rows + 1):
#    row = []
#    for j in range(cols + 1):
#        row.append(False)
#    canvas.append(row)

# Go through brush swipes, starting with rows
for i in range(rows):
    if row_swipes[i]: #then it should be gold
        for j in range(cols): #go through items in row i
            canvas[i][j] = not canvas[i][j] #[row][column]

# Go through column swipes
for i in range(cols):
    if col_swipes[i]:
        for j in range(rows):
            canvas[j][i] = not canvas[j][i]#[row][column]

# Count gold cells
gold_count = 0
for i in range(rows):
    for j in range(cols):
        if canvas[i][j]:
            gold_count += 1

# Output gold count
print(gold_count)



# Practice problem: Given a list of integers that's sorted from smallest to largest and a target value,
# return the index where that item is found or -1 if it's not in the list
def search(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if nums[middle] == target:
            return middle
        if target < nums[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1