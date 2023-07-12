import sys

input = sys.stdin.readline

n, m, k  = map(int, input().split())

c = {i + 1 : 0 for i in range(k)}

score = []

for i in range(k):
    f, d = map(int, input().split())
    c[i] = (f, d)
    score.append((i + 1, (m + 1) - c[i][1] + abs(1 - c[i][0])))

winner = sorted(score, key=lambda x : (x[1], x[0]))

print(winner[0][0])  