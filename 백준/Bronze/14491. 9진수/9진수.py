n = int(input())
result = ""

while n > 0:
    result = str(n % 9) + result
    n //= 9

print(result)