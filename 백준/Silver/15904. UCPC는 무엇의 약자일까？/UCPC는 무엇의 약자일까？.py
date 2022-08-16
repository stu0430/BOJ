X = ['U', 'C', 'P', 'C']
n = input()
r = ''
for x in n:
  if x == 'U' or x == 'C' or x == 'P':
    r += x
i = 0
l = ''
for x in r:
  if l == 'UCPC':
    break
  elif x == X[i]:
    l += x
    i += 1
if l == 'UCPC':
  print('I love UCPC')
else:
  print('I hate UCPC')