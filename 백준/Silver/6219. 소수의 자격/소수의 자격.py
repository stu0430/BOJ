import sys
 
def f(num,num2):
    num ,chk= str(num),0
    for i in num:
        if num2 == int(i): chk=1
    if chk == 1: return 1
    else: return 0
A,B,D = map(int,sys.stdin.readline().split())
a = [False,False] + [True] * 4000001
ans=0
for i in range(2,4000001):
    if a[i] == True:
        for j in range(i+i,4000001,i):
            a[j] = False
for i in range(A,B,1):
    if a[i] == True: ans = ans + f(i,D)
print(ans)