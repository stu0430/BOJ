s = input()

s = s.replace('pi', '!')
s = s.replace('ka', '!')
s = s.replace('chu', '!')

if len(s) == s.count('!'):
    print('YES')

else:
    print('NO')