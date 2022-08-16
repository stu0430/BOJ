n = int(input())
fibo_sim = [1,1,1]
for i in range(3, n):
    fibo_sim.append(fibo_sim[i-1] + fibo_sim[i-3])
if n == (1 or 2 or 3):
    print(1)
else:
    print(fibo_sim[-1])