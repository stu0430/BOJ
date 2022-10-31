import sys

input = sys.stdin.readline

k, n = map(int, input().split())

array = [int(input()) for i in range(k)]

start = 1

end = max(array)

while start <= end:
    mid = (start + end) // 2
    count = 0
    for i in array:
        count += i // mid
        
    if count >= n:
        start = mid + 1
        result = mid
    else:
        end = mid - 1
        
print(result)