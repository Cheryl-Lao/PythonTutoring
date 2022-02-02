# https://github.com/charlescchen/CCC-Solutions/blob/master/CCC-2018/Senior/Senior-2/S2.py
# CCC 2018 Junior 4/Senior 2: Sunflowers
#
# Author: Charles Chen
#
# If you look carefully, you will notice that in any correct
# table, the top left corner always contains the smallest number.
# You can solve this problem by first locating the smallest number
# by searching all 4 corners and then "rotating" the table back to
# the correct position depending on which corner the smallest number
# is located.

# Input
flowers = int(input())
measurements = []
for i in range(flowers):
    measurements.append(list(map(int, input().split())))

# Find location of smallest number
min_number = measurements[0][0]
row = 0
column = 0

if measurements[0][flowers - 1] < min_number:
    row = 0
    column = flowers - 1
    min_number = measurements[0][flowers - 1]
if measurements[flowers - 1][0] < min_number:
    row = flowers - 1
    column = 0
    min_number = measurements[flowers - 1][0]
if measurements[flowers - 1][flowers - 1] < min_number:
    row = flowers - 1
    column = flowers - 1
    minNumber = measurements[flowers - 1][flowers - 1]

# [[A, B, C],
#  [D, E, F],
#  [G, H, I]]

'''
90 degrees
[[C, F, I],
 [B, E, H],
 [A, D, G]]

180 degrees
[[I, H, G],
 [F, E, D],
 [C, B, A]]

270 degrees
[[G, D, A],
 [H, E, B],
 [I, F, C]]
'''
# Print Original Table
if row == 0 and column == 0:  # Normal Table (Flip 0 Degrees)
    for i in range(flowers):
        for j in range(flowers):
            print(measurements[i][j], end=" ")
        print()
elif row == 0 and column > 0:  # Flip 90 Degrees CCW
    for i in range(flowers - 1, -1, -1):
        for j in range(flowers):
            print(measurements[j][i], end=" ")
        print()
elif row > 0 and column > 0:  # Flip 180 Degrees CW/CCW
    for i in range(flowers - 1, -1, -1):
        for j in range(flowers - 1, -1, -1):
            print(measurements[i][j], end=" ")
        print()
else:  # Flip 90 Degrees CW (270 Degrees CCW)
    for i in range(flowers):
        for j in range(flowers - 1, -1, -1):
            print(measurements[j][i], end=" ")
        print()
