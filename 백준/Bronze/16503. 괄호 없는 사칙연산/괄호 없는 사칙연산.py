s = input().split()
k1, o1, k2, o2, k3 = int(s[0]), s[1], int(s[2]), s[3], int(s[4])

def calc(a, op, b):
    if op == '+':
        return a + b
    elif op == '-':
        return a - b
    elif op == '*':
        return a * b
    else:
        return int(a / b)

x = calc(calc(k1, o1, k2), o2, k3)
y = calc(k1, o1, calc(k2, o2, k3))

print(min(x, y))
print(max(x, y))