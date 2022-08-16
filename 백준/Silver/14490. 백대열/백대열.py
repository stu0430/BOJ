import math
n, m = map(int, input().split(':'))
gcd_n = math.gcd(n, m)
print(n//gcd_n, m//gcd_n, sep=':')