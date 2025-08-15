n = int(input())
totals = []

for i in range(n):
    data = list(map(int, input().split()))
    count = data[0]
    total = sum(data[1:count+1])
    totals.append(total)

totals.sort()

cumulative_sum = 0
result = 0

for i in range(n):
    cumulative_sum += totals[i]
    result += cumulative_sum

print(result)