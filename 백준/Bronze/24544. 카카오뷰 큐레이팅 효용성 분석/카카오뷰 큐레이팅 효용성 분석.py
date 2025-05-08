n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

print(sum(a))
print(sum([a[i] for i in range(n) if b[i] == 0]))