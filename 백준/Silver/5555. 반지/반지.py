s = input()
n = int(input())
cnt = 0
for i in range(n):
    ring = input()*2
    if s in ring:
        cnt +=1
print(cnt)