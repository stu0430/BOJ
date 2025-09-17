n = int(input())
a = list(map(int, input().split()))

cnt = {}
for i in a:
    cnt[i] = cnt.get(i, 0) + 1

if max(cnt.values()) <= (n + 1) // 2:
    print('YES')
    
else:
    print('NO')