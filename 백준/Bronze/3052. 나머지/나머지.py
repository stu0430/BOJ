L = []
L_2 = []
count = 0
for i in range(1, 11):
    a = int(input())
    L.append(a)
for j in L:
    if (j % 42) not in L_2:
        L_2.append(j % 42)
        count += 1
print(count)