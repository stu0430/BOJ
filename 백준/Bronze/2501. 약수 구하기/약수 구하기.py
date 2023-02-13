import sys

input = sys.stdin.readline

n, k = map(int, input().split())

array = [i for i in range(1, n + 1) if n % i == 0]
        
if len(array) < k:
    print(0)

else:
    print(array[k - 1])