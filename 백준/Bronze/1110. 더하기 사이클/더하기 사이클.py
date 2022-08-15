n = int(input())
if n < 10:
    new_n = '0' + str(n)
else:
    new_n = str(n)
new_n2 = new_n
cycle = 0
while True:
    new_n3 = str(int(new_n2[0]) + int(new_n2[1]))
    new_n3 = new_n3[-1]
    new_n2 = str(new_n2[1]) + new_n3
    cycle += 1
    if new_n2 == new_n:
        print(cycle)
        break