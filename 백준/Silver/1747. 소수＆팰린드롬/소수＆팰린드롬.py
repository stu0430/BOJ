import sys
n = int(sys.stdin.readline().rstrip())
result = 0
def isPrime(x):
    for i in range(2, int((x**0.5)+1)):
        if x % i == 0:
            return False
    return True
for i in range(n, 1000001):
    if i == 1:
        continue
    if str(i) == str(i)[::-1] and isPrime(i):
        result = i
        break
if result == 0:
    result = 1003001
print(result)