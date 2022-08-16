import sys
from copy import deepcopy
n = int(sys.stdin.readline())
lst = []
for i in range(n):
    a = sys.stdin.readline().rstrip()
    lst.append(a)
inc = deepcopy(lst)
dec = deepcopy(lst)
inc.sort()
dec.sort(reverse=True)
if lst == inc:
    print('INCREASING')
elif lst == dec:
    print('DECREASING')
else:
    print('NEITHER')