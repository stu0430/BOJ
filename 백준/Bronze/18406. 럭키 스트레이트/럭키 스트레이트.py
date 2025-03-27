n = input()

mid = len(n) // 2

if sum(map(int, n[:mid])) == sum(map(int, n[mid:])):
    print('LUCKY')
else:   
    print('READY')