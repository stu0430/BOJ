import sys

input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().rstrip()

i = 0
count = 0
result = 0

while i < (m - 1):
    if s[i:i + 3] == 'IOI':
        i += 2
        count += 1
        
        if count == n:
            result += 1
            count -= 1
    else:
        i += 1
        count = 0

print(result)