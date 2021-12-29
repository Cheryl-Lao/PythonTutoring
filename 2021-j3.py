#!/usr/bin/env python
# Answer based on https://github.com/charlescchen/CCC-Solutions/blob/master/CCC-2021/Junior/Junior-2/J2.py

previous = ""
instruction = ""
direction = ""

while True:
    instruction = input()
    if instruction == "99999":
        break

    num = instruction[:2] #Get the first 2 digits
    print(num)
    digitSum = int(num[:1]) + int(num[1:]) # Break down the first two digits

    if digitSum == 0:
        direction = previous
    elif (digitSum % 2) == 0: #if even
        previous = "right"
        direction = "right"
    else:
        previous = "left"
        direction = "left"

    print(direction, instruction[2:]) #print the direction and the last 3 digits

