import sys

input = sys.stdin.readline

n, k = map(int, input().split())
s = input().rstrip()

if k == 1:
    result = s
    
elif (n - k) % 2:
    result = s[k - 1:] + s[:k - 1]
    
else:
    result = s[k - 1:] + s[k - 2::-1]

print(result)