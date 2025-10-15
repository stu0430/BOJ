n = int(input())

if n == 0:
    print('NO')
else:
    power = 1
    powers_of_3 = []
    
    while power <= n:
        powers_of_3.append(power)
        power *= 3
    
    found = any(
        sum(powers_of_3[i] for i in range(len(powers_of_3)) if mask & (1 << i)) == n
        for mask in range(1 << len(powers_of_3))
    )
    
    print('YES' if found else 'NO')