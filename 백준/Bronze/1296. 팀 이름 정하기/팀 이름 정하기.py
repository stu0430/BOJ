name = input()
n = int(input())

t_name = sorted([input() for i in range(n)])

max_p, max_i = 0, 0

l, o, v, e = name.count('L'), name.count('O'), name.count('V'), name.count('E')

for i in range(n):
    L = l + t_name[i].count('L')
    O = o + t_name[i].count('O')
    V = v + t_name[i].count('V')
    E = e + t_name[i].count('E')
    
    p = ((L + O) * (L + V) * (L + E) * (O + V) * (O + E) * (V + E)) % 100
    
    if p > max_p:
        max_p = p
        max_i = i
        
print(t_name[max_i])