l = int(input())
a = int(input())
b = int(input())
c = int(input())
d = int(input())

print(l - max((a + c - 1) // c, (b + d - 1) // d))