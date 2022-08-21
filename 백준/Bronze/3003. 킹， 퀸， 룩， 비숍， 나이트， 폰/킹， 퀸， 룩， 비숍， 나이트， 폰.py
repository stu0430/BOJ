import sys
input = sys.stdin.readline
black = [1, 1, 2, 2, 2, 8]
white = list(map(int, input().split()))
piece_gap = [0] * 6
for i in range(6):
    piece_gap[i] = black[i] - white[i]
print(*piece_gap)