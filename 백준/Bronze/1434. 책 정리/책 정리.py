n, m = map(int, input().split())
a = list(map(int, input().split()))
m = list(map(int, input().split()))

for i in range(len(m)):
    for j in range(len(a)):
        if m[i] > a[j]:
            continue  
            
        a[j] -= m[i]
        break

print(sum(a))