import sys

input = sys.stdin.readline

n = int(input())
s = [list(map(int, input().split())) for _ in range(n)]

if n == 2:
    print('1 1')
    
else:
    a1 = (s[0][1] + s[0][2] - s[1][2]) // 2
    result = [a1] + [s[0][i] - a1 for i in range(1, n)]
    
    print(*result)