c = int(input())
for i in range(c):
    a = list(map(int, input().split()))
    ave = sum(a[1:])/a[0]
    high_score = 0
    for j in a[1:]:
        if j > ave:
            high_score += 1
    print('{0:.3f}%'.format((high_score/a[0])*100))