n = int(input())
Fibo = [0, 1]
for i in range(2,n+1):
    Fibo.append(Fibo[i-1]+Fibo[i-2])
if n == 0:
    print(0)
elif n == 1:
    print(1)
else:
    print(Fibo[-1])