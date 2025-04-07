n, q = map(int, input().split())

idx = 0
result = 2**63 - 1

for i in range(1, n + 1):
    p, k, c = map(int, input().split())
    
    cost = p + (q - 1) // k * ((q - 1) // k + 1) // 2 * c
    
    if cost < result:
        result = cost
        idx = i

print(idx, result)