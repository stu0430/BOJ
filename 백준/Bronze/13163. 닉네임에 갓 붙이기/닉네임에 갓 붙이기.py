import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    s = input().rstrip().split()
    print('god' + ''.join(s[1:]))