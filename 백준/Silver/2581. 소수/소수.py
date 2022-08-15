import sys
n = int(sys.stdin.readline())
m = int(sys.stdin.readline())
lst = []
for i in range(n,m+1):
    cnt = 0
    for j in range(i,0,-1):
        if i % j == 0:
            cnt +=1
    if cnt == 2:
        lst.append(i)
if len(lst) == 0:
    print(-1)
else:
    print(sum(lst), min(lst),sep='\n')