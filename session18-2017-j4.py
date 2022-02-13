"""

d = int(input())
hr = 12
mn = 0
counter = 0

#Loop through all of the possible times, minute-by-minute
for i in range(d):
    mn = int(mn)
    hr = int(hr)
    mn += 1
    if mn >= 60: #move onto the next hour
        mn -= 60
        if hr + 1 < 13:
            hr += 1
        else:
            hr = (hr + 1) % 12
    if mn < 10:
        mn = "0" + str(mn)
    mn = str(mn)
    hr = str(hr)
    time = hr + mn  #time is a string with all the digits of the time
    if len(time) == 3:
        if (int(time[2]) - int(time[1])) == (int(time[1]) - int(time[0])):
            counter += 1
    else:
        if ((int(time[3]) - int(time[2])) == (int(time[2]) - int(time[1]))) and (
                (int(time[2]) - int(time[1])) == (int(time[1]) - int(time[0]))):
            counter += 1

print(counter)

"""



def isArithmetic(digits):
    diff = digits[1] - digits[0]
    for i in range(len(digits) - 1):
        if digits[i+1] - digits[i] != diff:
            return False
    return True

d = int(input())
cycles_removed = d // 720 #key insight: the entire 12-hour period (720 minutes) has 31 arithmetic sequences in it so you can just add 31 for each 720 mintues without doing any more calculations
hr = (d % 720) // 60
mn = d % 60

counter = 0
seen_times = {} #"12":["34"], "1":["11", "23"]
currentTime = "12:00"

hours = []
hour = 12
for i in range(hr+1):
   if hour == 13:
       hour = 1
   hours.append(hour)
   hour += 1

count = 0
for i in range(len(hours)):

    # If you encountered it before already
    if hour in seen_times:
        count += len(seen_times[hour])
    else:
        possibilities = []
        if hours[i] > 9: # 2 digits
            digits = [hours[i]//10, hours[i]%10]
            diff = digits[1] - digits[0]
            digits.append(digits[1] + diff)
            digits.append(digits[2] + diff)

            if isArithmetic(digits)  and digits[2] >= 0 and digits[3] >= 0 and int(str(digits[2]) + str(digits[3])) < 60:
                possibilities.append([digits[2], digits[3]])

        else: # 1 digit
            # Loop through all possible 2nd digits (0, 1, 2, 3, 4, 5) 9:(0, 1, 2, 3, 4, 5)
            for j in range(6):
                digits = [hours[i], j]
                diff = digits[1] - digits[0]
                digits.append(digits[1] + diff)

                if isArithmetic(digits) and digits[1] >= 0 and digits[2] >= 0 and int(str(digits[1]) + str(digits[1])) < 60:
                    possibilities.append([digits[1], digits[2]])

        seen_times[hours[i]] = possibilities
        count += len(possibilities)

# deal with the last hour separately
# subtract out the number of items that aren't in the valid range in the last hour
last_hour = hours[len(hours)-1]
last_hour_options = seen_times[last_hour]

for i in range(len(last_hour_options)):
    minute_as_int = int(str(last_hour_options[i][0]) + str(last_hour_options[i][1]))

    if minute_as_int > mn:
        count -= 1

#There are 31 arithmetic sequences in every 12-hour cycle
count += cycles_removed * 31
print(count)

#hour_to_possibilities = {12: 34, 1: [11, 23, 35, 47, 59], 2: [10, 22, 34, 46, 58], 3: [21, 33, 45, 57], 4: [20, 32, 44, 56], 5: [31, 43, 55], 6: [30, 42, 54], 7: [41, 53], 8: [40, 52], 9: [51], 10: [], 11: [11]}


"""
minutes = 170
hours = 3

12:00 -> diff 1 12:34
1:00
1:11
1:23
1:35
1:47
1:59

2:00
2:10  -1
2:22
2:34
2:46
2:58
170
hr = 2
mn = 50
check minute < mn when hour == hr

3:00-

-calculate # of hours and minutes in the duration
[12, 1, 2]

"""