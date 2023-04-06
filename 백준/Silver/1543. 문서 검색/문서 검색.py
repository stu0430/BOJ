import sys

input = sys.stdin.readline

s = input().rstrip()
t = input().rstrip()

idx = 0
count = 0

for i in range(len(s)):
    if idx > i:
        continue
    
    if s[i:i + len(t)] == t:
        count += 1
        idx = i + len(t)
        
print(count)