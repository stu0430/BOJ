import sys

input = sys.stdin.readline

n, q = map(int, input().split())

row_count = [0] * 30001
col_count = [0] * 30001

max_row_count = 0
rows_with_max = n
max_col_count = 0
cols_with_max = n

for _ in range(q):
    t, a = map(int, input().split())
    
    if t == 1:
        row_count[a] += 1
        if row_count[a] > max_row_count:
            max_row_count = row_count[a]
            rows_with_max = 0
        if row_count[a] == max_row_count:
            rows_with_max += 1
    
    elif t == 2:
        col_count[a] += 1
        if col_count[a] > max_col_count:
            max_col_count = col_count[a]
            cols_with_max = 0
        if col_count[a] == max_col_count:
            cols_with_max += 1
    
    print(rows_with_max * cols_with_max)