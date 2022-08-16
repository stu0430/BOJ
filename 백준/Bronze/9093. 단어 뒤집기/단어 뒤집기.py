n = int(input())
for i in range(n):
    sen = input().split()
    for j in sen:
        print(j[::-1], end=' ')
    print()