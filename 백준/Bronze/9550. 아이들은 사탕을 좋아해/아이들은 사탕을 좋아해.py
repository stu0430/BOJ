t = int(input())
result = []

for _ in range(t):
    n, k = map(int, input().split())
    array = list(map(int, input().split()))
    result.append(sum(i // k for i in array))

print(*result, sep='\n')