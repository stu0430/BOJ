import sys

input = sys.stdin.readline

x, y, c = map(float, input().split())

start = 1
end = min(x, y)

while start + 0.001 <= end:
    mid = (start + end) / 2
    h1 = (x ** 2 - mid ** 2) ** 0.5
    h2 = (y ** 2 - mid ** 2) ** 0.5
    h = (h1 * h2) / (h1 + h2)
    
    if h >= c:
        start = mid
        result = mid
    else:
        end = mid

print(round(result, 3))