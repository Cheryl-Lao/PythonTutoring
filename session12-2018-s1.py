#sorting
lst = [8, 2, 3, 4, 5]
print(lst.sort()) # sorts in-place and changes the list -- doesn't copy
print(lst)

#print(sorted(lst)) # copies the list and sorts
#print(lst)

#Practice Problem:
#https://leetcode.com/problems/student-attendance-record-i/

"""
public class Solution {
    public boolean checkRecord(String s) {
        int countA = 0;
        for (int i = 0; i < s.length() && countA < 2; i++) {
            if (s.charAt(i) == 'A')
                countA++;
            if (i <= s.length() - 3 && s.charAt(i) == 'L' && s.charAt(i + 1) == 'L' && s.charAt(i + 2) == 'L')
                return false;
        }
        return countA < 2;
    }
}
"""


def CheckRecord(record):
    numA = 0
    i = 0
    while i < len(record) and numA < 2:
        if record[i] == "A":
            numA += 1
        if i <= len(record) - 3 and record [i] == 'L' and record [i+1] == 'L' and record [i+2] == 'L':
            return False
        i += 1
    return numA < 2

print(CheckRecord("PPALLL"))
print(CheckRecord("PPALLP"))

"""
#https://gist.github.com/LiamHz/e732c2b6f4e7d57af69cad01df1602b9
#Number of villages
N = int(input())
#List of village positions
villages = list()
for i in range(N):
    villages.append(float(input()))

#List of distances between villages
distances = list()

#Sort the villages, from small to large, based on their positions
villages.sort()

#First and last villages distances are infinite
for i in range(1, N - 1):
    #Calculate neighborhood size for each village other than the first and last
    distances.append( (villages[i+1] - villages[i]) / 2 + (villages[i] - villages[i - 1]) / 2 )

#Sort distances from small to large
distances.sort()

#Print Smallest
print(distances[0])




#https://github.com/charlescchen/CCC-Solutions/blob/master/CCC-2018/Senior/Senior-2/S2.py
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

if measurements[0][flowers-1] < min_number:
    row = 0
    column = flowers - 1
    min_number = measurements[0][flowers - 1]
if measurements[flowers-1][0] < min_number:
    row = flowers - 1
    column = 0
    min_number = measurements[flowers - 1][0]
if measurements[flowers-1][flowers-1] < min_number:
    row = flowers - 1
    column = flowers - 1
    minNumber = measurements[flowers - 1][flowers - 1]

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


"""


