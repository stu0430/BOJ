b,r = "",0

for i in list(input()):
    if i != b:
        r += 10
        b = i
    else:
        r += 5
        
print(r)