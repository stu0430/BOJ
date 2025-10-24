t = int(input())

for _ in range(t):
    s = input()
    
    num = '0' if '0' in s else '1'
    
    l = s.split(num)[0].count('!')
    r = s.split(num)[1].count('!') if len(s.split(num)) > 1 else 0
    
    if r > 0:
        num = '1'
    
    if l % 2 == 1:
        num = '0' if num == '1' else '1'
    
    print(num)