import sys

input = sys.stdin.readline

n = int(input())

start, end, d = [0] * 1000001, [0] * 1000001, [0] * 1000001

for _ in range(n):
    s, e = map(int, input().split())
    
    start[s] += 1
    end[e] += 1

for i in range(1, 1000001):
    d[i] = d[i - 1] + start[i] - end[i - 1]

q = int(input())
Q = list(map(int, input().split()))

for q in Q:
    print(d[q])