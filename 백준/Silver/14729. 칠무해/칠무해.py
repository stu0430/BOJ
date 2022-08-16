import sys
n = int(sys.stdin.readline().strip())
score = []
for _ in range(n):
    score.append(float(sys.stdin.readline().strip()))
score.sort()
print("\n".join("%.3f" % score[i] for i in range(7)))