import sys
from math import ceil

input = sys.stdin.readline

n = int(input())

result = 0

for i in range(ceil(n / 3), ceil(n / 2)):
    result += i - ceil((n - i) / 2) + 1
    
print(result)