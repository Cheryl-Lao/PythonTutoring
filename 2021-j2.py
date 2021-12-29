#!/usr/bin/env python
# Answer based on https://github.com/charlescchen/CCC-Solutions/blob/master/CCC-2021/Junior/Junior-2/J2.py

import math

names = []
bid_amounts = []
max_index = -1
max_bid = -math.inf

# Get the number of bids so that you know how many to expect
num_bids = int(input())

# Keep on looking for input until you reach the number of bids you expect
for i in range(num_bids):
    names.append(input())
    bid_amounts.append(int(input()))
    if bid_amounts[i] > max_bid:
        max_bid = bid_amounts[i]
        max_index = i

# Output winner
print(names[max_index])