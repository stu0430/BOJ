import sys

input = sys.stdin.readline

t = int(input())

for _ in range(t):
    n = input().rstrip()

    result = 0

    while n != '6174':
        max_number = int(''.join(sorted(n, reverse=True)))
        min_number = int(''.join(sorted(n)))
        
        n = str(max_number - min_number).zfill(4)

        result += 1

    print(result)