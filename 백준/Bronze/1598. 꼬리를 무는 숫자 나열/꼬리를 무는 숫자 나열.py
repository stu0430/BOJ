a, b = map(int, input().split())
a -= 1
b -= 1

a_x = a // 4
a_y = a % 4

b_x = b // 4
b_y = b % 4

print(abs(b_x - a_x) + abs(b_y - a_y))