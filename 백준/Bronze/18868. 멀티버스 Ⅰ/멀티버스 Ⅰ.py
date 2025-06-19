from collections import Counter

m, n = map(int, input().split())
array = [list(map(int, input().split())) for _ in range(m)]

for i in range(m):
    arr_sort = sorted(array[i])
    rank_dict = {val: idx + 1 for idx, val in enumerate(arr_sort)}
    array[i] = [rank_dict[val] for val in array[i]]

count = Counter(tuple(row) for row in array)
result = sum(count * (count - 1) // 2 for count in count.values())

print(result)