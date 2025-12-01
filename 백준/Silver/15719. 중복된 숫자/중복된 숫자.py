import sys

n = int(input())
sum_n = sum(range(1, n))
a = sys.stdin.readline().rstrip()

sum_num = 0
temp = ""

for char in a:
    if char.isdigit():
        temp += char
    else:
        if temp:
            sum_num += int(temp)
            temp = ""

if temp:
    sum_num += int(temp)

print(sum_num - sum_n)