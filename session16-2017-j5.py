N = int(input())
boards = input().split(" ")
L = [0]*2001
F = [0]*4001

for board in boards:
    L[int(board)] += 1

for i in range(0, len(L) - 1):
    for j in range(i, len(L)):
        if i == j:
            F[i + j] += L[i] // 2  # number of board// 2 gives you the width of the fence that you could create by matching up the same two boards together
        else:
            F[i + j] += min(L[i], L[j]) #

longest, size = 0, 0

for fenceLength in F:
    if fenceLength > longest:
        longest = fenceLength
        size = 1 #reset to 1 because you found a new longest possibility
    elif fenceLength == longest:
        size += 1

print(longest, size)

