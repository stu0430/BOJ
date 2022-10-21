import sys

input = sys.stdin.readline

n = int(input())

start = 0
end = n

result = 0
mid = 0

while start <= end:
    mid = (start + end) // 2
    
    if mid ** 2 >= n:
        end = mid - 1
        result = mid
    else:
        start = mid + 1

print(result)