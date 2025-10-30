isbn = input()

num = 0
flag = -1

for i in range(12):
    if isbn[i] == '*':
        flag = i
    else:
        num += int(isbn[i]) * (1 if i % 2 == 0 else 3)

checksum = int(isbn[-1])
multiplier = 1 if flag % 2 == 0 else 3

for digit in range(10):
    if (num + digit * multiplier + checksum) % 10 == 0:
        print(digit)
        break