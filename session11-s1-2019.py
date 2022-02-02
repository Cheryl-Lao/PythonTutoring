"""
original = [[1, 2],
            [3, 4]]

flips = input()

for i in range(len(flips)):
    if flips[i] == 'H':
        original[0][0], original[1][0] = original[1][0], original[0][0] # 1, 3 = 3, 1
        original[0][1], original[1][1] = original[1][1], original[0][1] # 2, 4 = 4, 2
    else:
        original[0][0], original[0][1] = original[0][1], original[0][0] # 1, 2 = 2, 1
        original[1][0], original[1][1] = original[1][1], original[1][0] # 3, 4 = 4, 3

print(original[0][0], original[0][1]) #3 4 after 1 H flip
print(original[1][0], original[1][1]) #1 2

"""



#Check if a list is sorted from smallest to largest
def isSorted(lst):
    sorted = True
    i = 1
    while i < len(lst):
        if(lst[i] < lst[i - 1]):
            sorted = False
        i += 1
    return sorted

print(isSorted([1, 2, 3, 4, 5]))
print(isSorted([5, 10, 15, 20, 25]))