n = int(input())

# Get measurements
inputs = input().strip().split(" ")

# Convert to ints
listed_tides = []
for i in range(len(inputs)):
    listed_tides.append(int(inputs[i]))

listed_tides.sort()
# Split list into high and low tides
low_tides = listed_tides[:int(n / 2)]
high_tides = listed_tides[int(n / 2):]

# Reverse the low tides because they should get smaller and smaller
low_tides = sorted(low_tides, reverse=True)

# Add the tides in the order that they occur
final_tides = []
for i in range(len(low_tides)):
    final_tides.append(low_tides[i])
    final_tides.append(high_tides[i])

# construct the final string
final_string = ""
for i in range(len(final_tides)):
    final_string += str(final_tides[i]) + " "

print(final_string)