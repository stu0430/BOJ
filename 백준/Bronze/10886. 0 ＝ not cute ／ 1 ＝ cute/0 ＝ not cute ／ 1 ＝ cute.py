N = int(input())
y = 0
n = 0
for i in range(N):
    cute = int(input())
    if cute == 1:
        y += 1
    elif cute == 0:
        n += 1
if y > n:
    print("Junhee is cute!")
elif y < n:
    print("Junhee is not cute!")