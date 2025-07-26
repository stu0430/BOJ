import sys

input = sys.stdin.readline

n, m = map(int, input().split())

flag = True

for _ in range(m):
    i = int(input())
    k = list(map(int, input().split()))
    
    for j in range(i - 1):
        if k[j] < k[j + 1]:
            flag = False
            break
        
    if not flag:
        break

print('Yes' if flag else 'No') 