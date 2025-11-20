n, m = map(int, input().split())
pattern = []
answer = [0, 0]

for _ in range(n):
    tmp = input().split()
    row = []
    for i in range(m):
        count = tmp[i].count('9')
        answer[0] += count
        row.append(count)
    pattern.append(row)

for row in pattern:
    if sum(row) > answer[1]:
        answer[1] = sum(row)

for j in range(m):
    col_sum = sum(pattern[k][j] for k in range(n))
    if col_sum > answer[1]:
        answer[1] = col_sum

print(answer[0] - answer[1])