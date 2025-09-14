import sys

input = sys.stdin.readline

n = int(input())
table = [None] + [input().rstrip() for _ in range(n)]

start = [(i, 1) for i in range(1, n+1)]
start.extend([(n, j) for j in range(2, 1001)])
        
result = 0

for i, j in start:
    r, c = i, j
    
    t_chars = []
    
    while 1 <= r <= n and 1 <= c <= 1000:
        if c <= len(table[r]):
            t_chars.append(table[r][c - 1])
            
        r -= 1
        c += 1
        
    if not t_chars:
        continue
    
    t = ''.join(t_chars)
    
    cnt1 = 0
    for k in range(len(t) - 4):
        if t[k:k + 5] == 'KUMOH':
            cnt1 += 1
    
    cnt2 = 0
    for k in range(len(t[::-1]) - 4):
        if t[::-1][k:k + 5] == 'KUMOH':
            cnt2 += 1
    
    result += max(cnt1, cnt2)

print(result)