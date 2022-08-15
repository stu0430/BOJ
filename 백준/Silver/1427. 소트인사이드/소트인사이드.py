n = int(input())
n = str(n)
lst = []
for i in n:
    lst.append(i)
lst.sort(reverse=True)
for j in lst:
    print(int(j),end='')