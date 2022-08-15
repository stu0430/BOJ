import sys
lst = []
for i in range(5):
    a = int(sys.stdin.readline())
    lst.append(a)
lst.sort()
print(sum(lst)//5,lst[2],sep='\n')