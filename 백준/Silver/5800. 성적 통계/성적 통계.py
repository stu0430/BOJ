K = int(input())
for i in range(K):
    score = []
    n = 0
    gap = []
    scores = list(map(int, input().split()))
    n = scores[0]
    score = scores[1:]
    for k in score:
        gap.append(k)
    gap.sort(reverse=True)
    lar_gap = []
    for j in range(len(gap)-1):
        x = gap[j] - gap[j+1]
        lar_gap.append(x)
    print('Class {0}'.format(i+1))
    print('Max {0}, Min {1}, Largest gap {2}'.format(max(score), min(score), max(lar_gap)))