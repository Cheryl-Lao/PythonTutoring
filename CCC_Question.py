"""

2022 S1 solution

n = 14
count = 0
seen_numbers = {}

for i in range((n // 5) + 1): # i is the number of 5s in your sequence
    part_4s = n - i * 5
    if part_4s % 4 == 0:
        count += 1

print(count)


"""

"""
2022 S2 Solution

int X for number of students who must be in the same group
A B

int Y for all the ones who CANNOT be together
A B

int G for the number of groups (3 per group)
A B C

output the number of violated constraints

each name is 1-10 uppercase letters
each name in a constaint appears in exactly one of the G groups

X + Y constraints
"""
num_together = int(input())

together_constraints = []


#set.union(set1, set2)


# 2022 S2 Solution
for i in range(num_together):
    constraint = input().split(" ")
    together_constraints.append(constraint)

num_apart = int(input())
apart_constraints = []

for i in range(num_apart):
    constraint = input().split(" ")
    apart_constraints.append(constraint)

num_groups = int(input())


groups = {}
for i in range(num_groups):
    group = set(input().split(" "))
    for person in group:
        groups[person] = set(group)

num_constraints_violated = 0
for constraint in together_constraints:
    if constraint[1] not in groups[constraint[0]]:
        num_constraints_violated += 1

for constraint in apart_constraints:
    if constraint[1] in groups[constraint[0]]:
        num_constraints_violated += 1

print(num_constraints_violated)
#dictionary with person as the key and their group members (including themselves)





