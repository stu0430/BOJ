t = int(input())

for _ in range(t):
    a, b = map(str, input().split())

    if sorted(list(a)) == sorted(list(b)):
        print(f'{a} & {b} are anagrams.')
        
    else:
        print(f'{a} & {b} are NOT anagrams.')