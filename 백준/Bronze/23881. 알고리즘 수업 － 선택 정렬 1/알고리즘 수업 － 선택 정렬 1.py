n, k = map(int, input().split())
a = list(map(int, input().split()))

count = 0
for i in range(n - 1, 0, -1):
    max_idx = a.index(max(a[:i + 1]))
    
    if max_idx != i:
        count += 1
        
        if count == k:
            print(min(a[max_idx], a[i]), max(a[max_idx], a[i]))
            exit()
            
        a[max_idx], a[i] = a[i], a[max_idx]

print(-1)