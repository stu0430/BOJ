t = int(input())
for i in range(t):
    word = []
    a, b = map(str, input().split())
    for j in b:
        word.append(j)
    del word[int(a)-1]
    for k in word:
        print(k,end='')
    print()