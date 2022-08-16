from math import gcd
n = int(input())
num1 = list(map(int, input().split()))
x = 1
y = 1
for i in num1:
    x *= i
m = int(input())
num2 = list(map(int, input().split()))
for j in num2:
    y *= j
K = str(gcd(x,y))
if len(K) > 9:
    K = K[-9:]
    print(K)
else:
    print(K)