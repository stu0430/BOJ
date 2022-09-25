import sys

input = sys.stdin.readline

n, m = map(int, input().split())
lst = list(map(int, input().split()))

def binary_search(lst, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        cnt = 1
        max_num = lst[0]
        min_num = lst[0]
        for i in range(1, len(lst)):
            max_num = max(max_num, lst[i])
            min_num = min(min_num, lst[i])
            if max_num - min_num > mid:
                cnt += 1
                max_num = lst[i]
                min_num = lst[i]
        if cnt <= m:
            target = mid
            end = mid - 1
        else:
            start = mid + 1
    return target
        
print(binary_search(lst, 0, 0, max(lst) - min(lst)))