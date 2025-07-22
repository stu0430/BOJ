x, y, p1, p2 = map(int, input().split())
X, Y = [p1], [p2]

result = -1

for i in range(1000):
    X.append(X[i] + x)
    Y.append(Y[i] + y)
    
    if X[i] + x in Y or Y[i] + y in X:
        result = min(X[i] + x, Y[i] + y)
        break
    
print(result)