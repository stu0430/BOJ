import sys

input = sys.stdin.readline

n = int(input())
array = list(input().rstrip())
l = 0
r = n - 1
count = 0

while l < r:
    if array[l] != array[r]:
        count += 1
    l += 1
    r -= 1
    
print(count)