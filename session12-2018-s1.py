#sorting
lst = [8, 2, 3, 4, 5]
print(lst.sort()) # sorts in-place and changes the list -- doesn't copy
print(lst)

#print(sorted(lst)) # copies the list and sorts
#print(lst)

#Practice Problem:
#https://leetcode.com/problems/student-attendance-record-i/

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


"""


