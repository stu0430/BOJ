n = int(input())
j = sorted(map(int, input().split()), reverse=True)
s = sorted(map(int, input().split()))
count = 0

for x in j:
    if x < s[-1]:
        count += 1
        s.pop()

print('YES' if count >= (n + 1) // 2 else 'NO')