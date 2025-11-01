import sys

input = sys.stdin.readline

n = int(input())
d = list(map(int, input().split()))

if n == 1 and d[0] == 1:
    print('Happy')
    
else:
    print('Happy' if (max(d) <= sum(d) // 2) else 'Unhappy')