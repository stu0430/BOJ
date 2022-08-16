l = int(input())
a = input()
lst = []
h = 0
for i in a:
    lst.append(ord(i))
for j in range(l):
    h += (lst[j]-96)*(31**j)
print(h%1234567891)