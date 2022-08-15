s = int(input())
X = 0
N = 0
for i in range(1, s+1):
    X += i
    N += 1
    if s == 2:
        print(1)
        break
    if X == s:
        print(N)
        break
    elif X > s:
        print(N-1)
        break