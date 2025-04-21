t = int(input())

for _ in range(t):
    n, m = map(int, input().split())
    
    array = [i for i in range(n, m + 1)]
    
    print(''.join(str(k) for k in array).count('0'))