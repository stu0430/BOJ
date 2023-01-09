import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    s = input().rstrip()
    
    if s == 'P=NP':
        print('skipped')
        
    else:
        print(sum(map(int, s.split('+'))))