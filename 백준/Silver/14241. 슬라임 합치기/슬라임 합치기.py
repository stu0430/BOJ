import sys
input = sys.stdin.readline
n = int(input())
slime = list(map(int,input().split()))
score = 0
for i in range(len(slime)-1):
    score += slime[0] * slime[1]
    slime[1] += slime[0]
    del slime[0]
print(score)