import sys

input = sys.stdin.readline

n = int(input())
t = [[0] * 5 for _ in range(5)]

mx = -1
x,y = -1,-1

for _ in range(n):
    a = list(map(int, input().split()))
    for i in range(5):
        for j in range(i + 1, 5):
            if a[i] == 1 and a[j] == 1:
                t[i][j] += 1

for i in range(5):
    for j in range(i + 1, 5):
        if t[i][j] > mx:
            mx = t[i][j]
            x = i
            y = j

print(mx)
print(' '.join('1' if i == x or i == y else '0' for i in range(5)))