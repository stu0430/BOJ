n, k = map(int, input().split())
x = sorted(map(int, input().split()))

result = 0
idx = -1

for i in x:
    if i <= idx:
        continue
    
    idx = i + k
    result += 1

print(result)