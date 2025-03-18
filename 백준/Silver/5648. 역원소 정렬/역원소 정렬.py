import sys
input = sys.stdin.read

n, *e = input().split()
n = int(n)

for i in range(n):
    e[i] = e[i][::-1]
    
print(*sorted(list(map(int, e))), sep='\n')