import sys

sys.setrecursionlimit(10**6)
input = sys.stdin.readline

t = int(input())

d = [0] * 10001

def fibo(x):
    if x == 1 or x == 2:
        return 1
    
    if d[x] != 0:
        return d[x]
    
    d[x] = fibo(x - 1) + fibo(x - 2)
    return d[x]

for i in range(t):
    p, q = map(int, input().split())
    print(f"Case #{i + 1}: {fibo(p) % q}")