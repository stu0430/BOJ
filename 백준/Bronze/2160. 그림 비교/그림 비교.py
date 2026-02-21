n = int(input())
min_diff = 35
array = [1, 2]

pictures = [[list(input().strip()) for _ in range(5)] for _ in range(n)]

for i in range(n - 1):
    for j in range(i + 1, n):
        diff_count = 0
        
        for row in range(5):
            for col in range(7):
                if pictures[i][row][col] != pictures[j][row][col]:
                    diff_count += 1
                    
        if diff_count < min_diff:
            min_diff = diff_count
            array = [i + 1, j + 1]

print(*array)