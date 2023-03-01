a = input()
b = input()

array = [0] * 26

for i in a:
    array[ord(i) - 97] += 1

for i in b:
    array[ord(i) - 97] -= 1

print(sum([abs(i) for i in array]))