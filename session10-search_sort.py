#https://www.hackerearth.com/practice/algorithms/sorting/insertion-sort/visualize/
#Bubblesort
#Keep on swapping elements until you get to the end
# https://www.geeksforgeeks.org/bubble-sort/

def bubbleSort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):

        # Last i elements are already in place
        for j in range(0, n-i-1):

            # traverse the array from 0 to n-i-1
            # Swap if the element found is greater
            # than the next element
            if arr[j] > arr[j+1] :
                arr[j], arr[j+1] = arr[j+1], arr[j]

# Driver code to test above
arr = [64, 34, 25, 12, 22, 11, 90]

bubbleSort(arr)

print (arr)



def insertionSort(arr):

    # Traverse through 1 to len(arr)
    for i in range(1, len(arr)):

        key = arr[i]

        # Move elements of arr[0..i-1], that are
        # greater than key, to one position ahead
        # of their current position
        j = i-1
        while j >= 0 and key < arr[j] :
                arr[j + 1] = arr[j]
                j -= 1
        arr[j + 1] = key


# Driver code to test above
arr = [12, 11, 13, 5, 6]
insertionSort(arr)
print(arr)

# If you have a sorted list and want to find an element in it
# Practice problem: Given a list of integers that's sorted from smallest to largest and a target value,
# return the index where that item is found or -1 if it's not in the list
def binary_search(nums, target):
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

my_nums = [1, 2, 3, 4, 5, 6, 7, 8]
print(binary_search(my_nums, 5))




#Practice Problem: Sort heights from shortest to tallest
"""
num_people = int(input())
heights = []
# read in all the heights
for i in range(num_people):
    heights.append(int(input()))

#sort the height list
insertionSort(heights)
print(heights)
"""

#Practice Problem: Modify the binary search function to work on lists sorted largest to smallest
"""
def binary_search_reverse(nums, target):
    left, right = 0, len(nums) - 1
    while left <= right:
        middle = left + (right - left) // 2
        if nums[middle] == target:
            return middle
        if target > nums[middle]:
            right = middle - 1
        else:
            left = middle + 1
    return -1

my_nums = [5, 4, 3, 2, 1]
print(binary_search_reverse(my_nums, 4))
"""


#2019 S1
"""
original = [[1, 2],
            [3, 4]]

flips = input()

for i in range(len(flips)):
    if flips[i] == 'H':
        original[0][0], original[1][0] = original[1][0], original[0][0]
        original[0][1], original[1][1] = original[1][1], original[0][1]
    else:
        original[0][0], original[0][1] = original[0][1], original[0][0]
        original[1][0], original[1][1] = original[1][1], original[1][0]

print(original[0][0], original[0][1])
print(original[1][0], original[1][1])

"""


