import sys

input = sys.stdin.readline

a, d, k = map(int, input().split())
d /= 100
k /= 100

probs = []
win = d
while win < 1:
    probs.append(win)
    win += win * k
probs.append(1.0)

lose = [1 - probs[0]]
for i in range(1, len(probs) - 1):
    lose.append(lose[-1] * (1 - probs[i]))

result = 0
for i, p in enumerate(probs):
    if i == 0:
        px = p
    else:
        px = lose[i-1] * p
    reward = a * (i + 1)
    result += reward * px

print(result)