import sys
input = sys.stdin.readline
n = int(input())
m = list(map(int,input().split()))
t = int(input())
for i in range(t):
    start,end = map(int,input().split())
    print(sum(m[start:end+1]))