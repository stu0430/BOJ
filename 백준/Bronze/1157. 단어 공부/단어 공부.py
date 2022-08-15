from collections import Counter
word = input()
word = word.lower()
lst = []
for i in word:
    lst.append(i)
cnt = Counter(lst).most_common()
if len(cnt) > 1 and cnt[0][1] == cnt[1][1]:
    print('?')
else:
    print(cnt[0][0].upper())