import sys

input = sys.stdin.readline

t = int(input())

for i in range(t):
    equ1 = list(map(int, input().split()))
    equ2 = list(map(int, input().split()))
    equ3 = list(map(int, input().split()))
  
    b = [equ1[-1], equ2[-1], equ3[-1]]
    
    detA = equ1[0] * (equ2[1] * equ3[2] - equ2[2] * equ3[1]) - \
           equ1[1] * (equ2[0] * equ3[2] - equ2[2] * equ3[0]) + \
           equ1[2] * (equ2[0] * equ3[1] - equ2[1] * equ3[0])
           
    detA1 = b[0] * (equ2[1] * equ3[2] - equ2[2] * equ3[1]) - \
            equ1[1] * (b[1] * equ3[2] - equ2[2] * b[2]) + \
            equ1[2] * (b[1] * equ3[1] - equ2[1] * b[2])
        
    detA2 = equ1[0] * (b[1] * equ3[2] - equ2[2] * b[2]) - \
            b[0] * (equ2[0] * equ3[2] - equ2[2] * equ3[0]) + \
            equ1[2] * (equ2[0] * b[2] - b[1] * equ3[0])
        
    detA3 = equ1[0] * (equ2[1] * b[2] - b[1] * equ3[1]) - \
            equ1[1] * (equ2[0] * b[2] - b[1] * equ3[0]) + \
            b[0] * (equ2[0] * equ3[1] - equ2[1] * equ3[0])
            
    print(detA1, detA2, detA3, detA)
    
    if detA == 0:
        print('No unique solution')
    else:
        x = detA1 / detA
        y = detA2 / detA
        z = detA3 / detA
        solutions = [x, y, z]
        print('Unique solution: ', end='')
        for solution in solutions:
            if -0.0005 < solution < 0.0005:
                print('0.000', end=' ')
            else:
                print("%0.3f" % solution, end=' ')
        print()
    print()