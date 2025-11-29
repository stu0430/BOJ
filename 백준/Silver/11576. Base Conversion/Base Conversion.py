a, b = map(int, input().split())
m = int(input())
digits = list(map(int, input().split()))

num_10 = 0
for i in range(m):
    num_10 += digits[i] * (a ** (m - i - 1))

result = []
while num_10:
    result.append(str(num_10 % b))
    num_10 //= b

print(' '.join(result[::-1]))