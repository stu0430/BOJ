import sys

input = sys.stdin.readline

STR, DEX, INT, LUK, N = map(int, input().split())
cnt = 0
stat_sum = STR + DEX + INT + LUK
average = stat_sum / 4

while average < N:
    stat_sum += 1
    average = stat_sum / 4
    cnt += 1

print(cnt)