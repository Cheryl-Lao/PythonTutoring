
N = int(input())

line1 = input().split(" ")
line2 = input().split(" ")

result = 0
team1score = 0
team2score = 0


for i in range (N):
    team1score += int(line1[i])
    team2score += int(line2[i])
    if team2score == team1score:
        result = i + 1 #because the answer should be based on 1
print(result)