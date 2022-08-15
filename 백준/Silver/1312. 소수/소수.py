a,b,n = map(int, input().split())
c = 0
for i in range(n+1):
    c = a//b
    a = a%b * 10
print(c)