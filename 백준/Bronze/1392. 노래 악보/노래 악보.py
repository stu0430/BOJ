n, q = map(int, input().split())
array = [int(input()) for _ in range(n)]

for _ in range(q):
    t = int(input())
    
    for i in range(n):
        if t < sum(array[:i + 1]):
            print(i + 1)
            break