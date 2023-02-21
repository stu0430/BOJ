import sys

input = sys.stdin.readline

t = int(input())

result = []
a = [300, 60, 10]

for i in a:
    result.append(t // i)
    t %= i
    
if t != 0:
    print(-1)
else:
    print(*result)