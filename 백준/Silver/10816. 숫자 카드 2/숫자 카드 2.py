import sys

input = sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))

m = int(input())
arr_2 = list(map(int, input().split()))

cnt = [0] * 20000001
for num in arr:
    cnt[num] += 1

for key in arr_2:
    print(cnt[key], end=' ')