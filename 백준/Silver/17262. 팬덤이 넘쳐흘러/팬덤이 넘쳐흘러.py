import sys

input = sys.stdin.readline

n = int(input())
 
array = [list(map(int, input().split())) for _ in range(n)]
 
s = sorted(array, reverse=True)
e = sorted(array, key=lambda x:x[1])

if (s[0][0] - e[0][1]) < 0:   
    print(0)   
    
else:
    print(s[0][0] - e[0][1])