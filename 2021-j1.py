#!/usr/bin/env python
# Answer from https://github.com/charlescchen/CCC-Solutions/blob/master/CCC-2021/Junior/Junior-1/J1.py

temperature = int(input()) # keyboard input

# Calculate pressure

#P = 5 × B − 400 where B is the temperature nat which water begins to boil in C

pressure = 5 * temperature - 400
print(pressure)

# Determine location relative to sea level
if pressure > 100:
    print(-1) # Below sea level
elif pressure == 100:
    print(0) # At sea level
else:
    print(1) # In this case, pressure < 100 and it's above sea level