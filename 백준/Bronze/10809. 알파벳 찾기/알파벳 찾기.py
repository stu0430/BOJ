s = list(input())
setS = list(set(s))
abc = []
result = []
a = ord('a')
z = ord('z')
for i in range(a, z+1):
    abc.append(chr(i))
for i in range(len(abc)):
    result.append(-1)
for i in setS:
    result[abc.index(i)] = s.index(i)
for j in result:
    print(j, end=' ')