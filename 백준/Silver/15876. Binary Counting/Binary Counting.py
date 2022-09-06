import sys

input = sys.stdin.readline

n, k = map(int, input().split())

lst = [bin(i).replace('0b','') for i in range(0,90)]
Jinsu = []

for i in lst:
    if len(i) != 1:
        lst[lst.index(i)] = list(i)
        
lst = [int(i) for lst2 in lst for i in lst2]

x = k-1
while True:
    if x >= len(lst)-1:
        break
    else:
        Jinsu.append(lst[x])
        x += n
        
if len(Jinsu) >= 5:   
    print(*Jinsu[:5])
else:
    print(*Jinsu)