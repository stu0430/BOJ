import sys

input = sys.stdin.readline

n = int(input())

array = [1, 5, 10, 50]

result = set()

for i in range(n + 1):
    for j in range(n + 1 - i):
        for k in range(n + 1 - i - j):
            result.add(i + (5 * j) + (10 * k) + (50 * (n - i - j - k)))
                    
print(len(result))