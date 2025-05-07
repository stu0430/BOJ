n, q = map(int, input().split())
array = list(map(int, input().split()))

for _ in range(q):
    query = list(map(int, input().split()))
    
    if query[0] == 1:
        a, b = query[1], query[2]
        print(sum(array[a - 1:b]))
        
        array[a - 1], array[b - 1] = array[b- 1], array[a - 1]
        
    else:
        a, b, c, d = query[1], query[2], query[3], query[4]
        print(sum(array[a - 1:b]) - sum(array[c - 1:d]))