from collections import Counter
import sys
lst = []
for i in range(10):
    a = int(sys.stdin.readline())
    lst.append(a)
cnt = Counter(lst).most_common()
print(sum(lst)//10, cnt[0][0],sep='\n')