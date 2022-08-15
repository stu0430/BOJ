def Rev(x):
    x = str(x)
    X = int(x[::-1])
    return X

a,b = map(int,input().split())
a = Rev(a)
b = Rev(b)
c = Rev(a+b)
print(c)