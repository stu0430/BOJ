x, y = map(int, input().split())
A = set(map(int, input().split()))
B = set(map(int, input().split()))
C = list(A - B)
print(len(C))
C.sort()
for i in C:
    print(i, end=' ')