s = input()
lst = []
for i in range(len(s)):
    lst.append(s)
    s = s[1:]
lst.sort()
for j in lst:
    print(j)