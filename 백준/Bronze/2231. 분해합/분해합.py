n = int(input())
hap = 0
for i in range(1,n+1):
    x = 0
    for j in str(i):
        x += int(j)
    if i + x == n:
        hap = i
        break
if hap == 0:
    print(0)
else:
    print(hap)