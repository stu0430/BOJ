n = int(input())
size = list(map(int,input().split()))
t, p = map(int,input().split())

cnt = 0

for i in size:
    if i == 0:
        continue
    
    elif i <= t:
        cnt += 1
        
    elif i % t == 0:
        cnt += i // t
        
    else:
        cnt += i // t + 1

print(cnt)
print(n // p, n % p)