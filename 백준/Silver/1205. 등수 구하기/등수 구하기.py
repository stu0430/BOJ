n, s, p = map(int, input().split())

if n == 0:
    print(1)
    exit()

rank = list(map(int, input().split()))

r = 1
for score in rank:
    if score > s:
        r += 1

if r > p:
    print(-1)
else:
    if rank.count(s) > 0 and r + rank.count(s) - 1 >= p:
        print(-1)
    else:
        print(r)