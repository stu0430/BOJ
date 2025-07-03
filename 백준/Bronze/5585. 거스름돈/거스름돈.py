changes = [500, 100, 50, 10, 5, 1]

t = int(input())

pay = 1000 - t
count = 0

for i in changes :
    count += pay // i
    pay %= i

print(count)