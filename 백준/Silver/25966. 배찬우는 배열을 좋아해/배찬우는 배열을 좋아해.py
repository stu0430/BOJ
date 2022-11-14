import sys

input = sys.stdin.readline

n, m, q = map(int, input().split())

array = [list(map(int, input().split())) for i in range(n)]

for i in range(q):
    query = list(map(int, input().split()))
    
    if query[0] == 0:
        array[query[1]][query[2]] = query[3]
        
    elif query[0] == 1:
        swap = array[query[1]]
        array[query[1]] = array[query[2]]
        array[query[2]] = swap
            
for j in array:
    print(*j)