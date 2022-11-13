import sys

input = sys.stdin.readline

l, r = input().rstrip().split()

count = 0

if len(l) != len(r):
    print(0)
    
else:
    for i in range(len(r)):
        if l[i] == r[i] and l[i] == '8':
            count += 1
        elif l[i] != r[i]:
            break
            
    print(count)