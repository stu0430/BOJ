import sys

input = sys.stdin.readline

count = 1

while True:
    n, m, p, q = map(int, input().split())
    
    if n == 0 and m == 0 and p == 0 and q == 0:
        break
    
    else:
        matrix_a = []
        matrix_b = []
        multipli_matrix = [[0] * q for i in range(n)]

        for i in range(n):
            matrix_a.append(list(map(int, input().split())))

        for j in range(p):
            matrix_b.append(list(map(int, input().split())))

        print(f'Case #{count}:')

        if m == p:
            for i in range(n):
                print('| ', end='')
                for j in range(q):
                    x = []
                    for l in range(m):
                        x.append(matrix_a[i][l] * matrix_b[l][j])    
                    multipli_matrix[i][j] = sum(x)
                    print(multipli_matrix[i][j], end=' ')
                print('|', end='\n')
        else:
            print('undefined')
            
        count += 1