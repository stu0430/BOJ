n = int(input())
S = list(map(int, input().split()))
X = list(set(S))
X.sort()
for i in X:
    print(i, end=' ')