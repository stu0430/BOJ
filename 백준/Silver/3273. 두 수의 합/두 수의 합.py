import sys

input = sys.stdin.readline

n = int(input())
array = sorted(list(map(int, input().split())))
x = int(input())

result = 0
left, right = 0, n - 1

while left < right:
    s = array[left] + array[right]
    
    if s == x:
        result += 1
        left += 1
        
    elif s > x:
        right -= 1
        
    elif s < x:
        left += 1

print(result)