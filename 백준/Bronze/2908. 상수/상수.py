a, b = map(str, input().split())
lst_a = []
lst_b = []
for i in a:
    lst_a.append(int(i))
for i in b:
    lst_b.append(int(i))
lst_a.reverse()
lst_b.reverse()
new_a = lst_a[0]*100 + lst_a[1]*10 + lst_a[2]
new_b = lst_b[0]*100 + lst_b[1]*10 + lst_b[2]
if new_a > new_b:
    print(new_a)
elif new_a < new_b:
    print(new_b)