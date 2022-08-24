import sys

input = sys.stdin.readline
n = int(input())
lst = []

for i in range(n):
    word = input().rstrip()
    if not [len(word),word] in lst:
        lst.append([len(word),word])
        
lst.sort()
lst = [k for [j,k] in lst]
print(*lst, sep="\n")