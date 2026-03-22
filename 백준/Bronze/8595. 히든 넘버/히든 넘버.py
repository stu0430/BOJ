n = int(input())
s = input()
reuslt = 0
num = ''

for c in s:
    if c.isdigit():
        num += c
        
    else:
        if num:
            reuslt += int(num)
            num = ''
if num:
    reuslt += int(num)

print(reuslt)