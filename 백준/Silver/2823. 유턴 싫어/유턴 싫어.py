import sys

input = sys.stdin.readline

r, c = map(int, input().split())

array = [list(input().rstrip()) for i in range(r)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

result = 0

for i in range(r):
    for j in range(c):
        if array[i][j] == '.':
            flag = 0
            
            for k in range(4):
                nx = i + dx[k]
                ny = j + dy[k]
                
                if 0 <= nx < r and 0 <= ny < c:
                    if array[nx][ny] == '.':
                        flag += 1
                        
            if flag == 1:
                result += 1
                
if result == 0:
    print(0)
else:
    print(1)