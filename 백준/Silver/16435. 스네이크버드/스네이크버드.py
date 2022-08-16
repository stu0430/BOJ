n,l = map(int,input().split())
fruits = list(map(int,input().split()))
fruits.sort()
for i in fruits:
    if l >= i:
        l += 1
print(l)