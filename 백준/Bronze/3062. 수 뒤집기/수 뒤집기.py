t = int(input())

for _ in range(t):
    n = input()
    
    result = str(int(n) + int(n[::-1]))
    
    if result == result[::-1]:
        print('YES')
    else:
        print('NO')