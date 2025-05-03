n = int(input())

board = [[0 for _ in range(500)] for _ in range(500)]
result = 0

for _ in range(n):
    x1, y1, x2, y2 = map(int,input().split())
    for i in range(y1, y2):
        for j in range(x1, x2):
            board[i][j] += 1
            
for row in range(500):
    for col in range(500):
        if board[row][col] > 0:
            result += 1
            
print(result)