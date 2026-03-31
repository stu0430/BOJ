n = int(input())
m, k = map(int, input().split())
a = sorted(map(int, input().split()), reverse=True)

total_sum = sum(a)
target = m * k

if target > total_sum:
    print('STRESS')
    
else:
    result = 0
    for i in range(n):
        result += a[i]        
        if result >= target:
            print(i + 1)
            break