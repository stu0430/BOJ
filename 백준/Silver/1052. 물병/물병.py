import sys

input = sys.stdin.readline

n, k = map(int, input().rstrip().split())

count = 0

while True:
    if bin(n).count('1') <= k:
        break
        
    n += 1
    count += 1
    
print(count)