t = int(input())

for case in range(1, t + 1):
    a, b = map(int, input().split())
    
    cube_root_a = int(a ** (1/3))
    while cube_root_a ** 3 < a:
        cube_root_a += 1
    
    cube_root_b = int(b ** (1/3))
    while (cube_root_b + 1) ** 3 <= b:
        cube_root_b += 1
    
    count = max(0, cube_root_b - cube_root_a + 1)
    
    print(f'Case #{case}: {count}')