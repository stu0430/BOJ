import sys

input = sys.stdin.readline

n = int(input())
board = [0] * n
result = 0

def is_safe(row):
    for i in range(row):
        if board[i] == board[row] or abs(row - i) == abs(board[row] - board[i]):
            return False
    return True

def solve(row):
    global result
    if row == n:
        result += 1
        return
    
    for col in range(n):
        board[row] = col
        if is_safe(row):
            solve(row + 1)

solve(0)
print(result)