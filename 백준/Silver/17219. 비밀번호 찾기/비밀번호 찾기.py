import sys
input = sys.stdin.readline
n,m = map(int,input().split())
ad_ps = {}
for i in range(n):
    adress,password = map(str,input().rstrip().split())
    ad_ps[adress] = password
for j in range(m):
    find_password = input().rstrip()
    print(ad_ps[find_password])
    