n = int(input())
t = list(map(int, input().split()))
t.sort()

m = 0
if n % 2 == 1:
    m = t.pop(-1)
    
loss = [t[i] + t[-i-1] for i in range(n // 2)] 
loss.append(m)

print(max(loss))