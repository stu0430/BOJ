n = int(input())
m = int(input())

result = 0

if n == 1:
    result += 8 * m
    
elif n == 5:
    result += 8 * m + 4

else:
    if m % 2 == 1:
        result += 5 - n

    else:
        result += n - 1

    result += 4 * m

print(result)