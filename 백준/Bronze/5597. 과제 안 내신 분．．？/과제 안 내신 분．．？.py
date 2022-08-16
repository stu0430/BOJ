std = [i for i in range(1,31)]
for i in range(28):
    a = int(input())
    std.remove(a)
std.sort()
for j in std:
    print(j)