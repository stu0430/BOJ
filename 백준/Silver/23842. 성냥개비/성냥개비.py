n = int(input())
a = [6, 2, 5, 5, 4, 5, 6, 3, 7, 6]

n -= 4

flag = False
for num1 in range(100):
    if flag:
        break
    
    for num2 in range(100):
        result = num1 + num2
        if result >= 100:
            break
        
        i, j = divmod(num1, 10)
        l, k = divmod(num2, 10)
        h, g = divmod(result, 10)
        
        if a[i] + a[j] + a[l] + a[k] + a[h] + a[g] == n:
            print(f"{i}{j}+{l}{k}={h}{g}")
            flag = True
            break

if not flag:
    print('impossible')