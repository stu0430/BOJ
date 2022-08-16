n,d = map(int,input().split())
lst = [str(i) for i in range(1,n+1) if str(d) in str(i)]
cnt = 0
for j in lst:
    cnt += j.count(str(d))
print(cnt)