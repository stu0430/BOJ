import sys

input = sys.stdin.readline

n = int(input())
company = dict()

for _ in range(n):
    name, status = input().rstrip().split()

    if status == 'enter':
        company[name] = status

    else:
        del company[name]

company = sorted(company.keys(), reverse=True)

print(*company, sep='\n')