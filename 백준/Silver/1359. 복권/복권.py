from itertools import combinations

n, m, k = map(int, input().split())

nums = list(range(1, n + 1))
lotto = list(combinations(nums, m))

total = 0

for temp in lotto:
    for s in lotto:
        count = sum(1 for num in temp if num in s)
        if count >= k:
            total += 1

print(total / (len(lotto) ** 2))