import sys
input = sys.stdin.readline
n,q = map(int,input().split())
speed = list(map(int,input().split()))
for i in range(q):
    start,end = map(int,input().split())
    speed_sum = 0
    for j in range((end-start)):
        speed_sum += abs(speed[start] - speed[start-1])
        start += 1
    print(speed_sum)