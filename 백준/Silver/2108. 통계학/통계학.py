import sys
from collections import Counter
n = int(sys.stdin.readline())
lst = []
for i in range(n):
    a = int(sys.stdin.readline())
    lst.append(a)
print(round(sum(lst)/n))
lst.sort()
print(lst[round(n//2)])
cnt = Counter(lst).most_common()
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print(cnt[1][0])
else:
    print(cnt[0][0])
print(max(lst)-min(lst))