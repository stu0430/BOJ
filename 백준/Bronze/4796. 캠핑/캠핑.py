import sys

input = sys.stdin.readline

count = 1

while True:
    l, p, v = map(int, input().split())
    
    if l == 0 and p == 0 and v == 0:
        break
    
    print(f'Case {count}: {(v // p) * l + min(v % p, l)}')
    
    count += 1