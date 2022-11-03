import sys

input = sys.stdin.readline

n, k = map(int, input().split())

array = [int(input()) for i in range(n)]
start, end = 1, max(array)

while start <= end:
    count = 0
    mid = (start + end) // 2
    
    for i in array:
        count += (i // mid)
        
    if count >= k:
        result = mid
        start = mid+1
        
    else:
        end = mid-1

print(result)