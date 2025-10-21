import sys

input = sys.stdin.readline

n = int(input())
array = [0] + list(map(int, input().split()))

cnt = 0
for i in range(1, n + 1):
    if array[i] == i:
        array[i] = n if i == 1 else 1
        cnt += 1

print(cnt)
print(' '.join(map(str, array[1:])))