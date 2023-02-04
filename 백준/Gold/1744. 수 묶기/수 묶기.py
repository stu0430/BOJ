import sys

input = sys.stdin.readline

N = int(input())

p = []
m = []
result = 0

for i in range(N):
    n = int(input())
        
    if n == 1:
        result += 1
        
    elif n > 0:
        p.append(n)
        
    else:
        m.append(n)
    
p.sort(reverse=True)
m.sort()

for i in [p, m]:
    if len(i) % 2 == 1:
        for j in range(0, len(i) - 1, 2):
            result += i[j] * i[j + 1]

        result += i[-1]

    else:
        for j in range(0, len(i), 2):
            result += i[j] * i[j + 1]

print(result)