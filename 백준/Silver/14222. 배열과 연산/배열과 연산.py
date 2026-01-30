import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

a.sort()

i = 0
while i < n:
    if i + 1 == a[i]:
        i += 1
        continue
    
    if i + 1 < a[i]:
        print(0)
        exit()
    
    a[i] += k
    a[i:] = sorted(a[i:])

print(1)