import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    state = list(map(int, input().split()))

    X = int(''.join(map(str, x)))
    Y = int(''.join(map(str, y)))

    result = 0

    for i in range(n):
        temp = int(''.join(map(str, state[i:i + m] + state[:max(0, i + m - n)])))
        
        if X <= temp <= Y:
            result += 1

    print(result)