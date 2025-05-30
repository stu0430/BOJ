n, k, a = map(int, input().split())
result = 99999999999999

for _ in range(n):
    t, s = map(int, input().split())

    result = min(result, k // a + (k // (a * t) + (0 if k % (a * t) else -1)) * s)
    
print(result)