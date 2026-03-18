import sys
from collections import Counter

input = sys.stdin.readline

n = int(input())
brands = list(map(int, input().split()))
count = Counter(brands)

uniq = sorted(count.keys())

result = 0

for k in range(1, max(uniq) + 1):
    flag = True
    product = 1
    
    for num in range(1, k + 1):
        if num in count:
            product *= count[num]
        else:
            flag = False
            break
        
    if flag:
        result += product

print(result)