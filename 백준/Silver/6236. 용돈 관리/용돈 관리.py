import sys

input = sys.stdin.readline

n, m = map(int, input().split())

array = [int(input()) for _ in range(n)]
start, end = max(array), sum(array)

result = 0

while start <= end:
    total = 0
    count = 1
    mid = (start + end) // 2
    
    for i in array:
        if total + i > mid:
            count += 1
            total = i
            
        else:
            total += i
            
    if count > m:
        start = mid + 1
        
    else:
        result = mid
        end = mid - 1
        
print(result)