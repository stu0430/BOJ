import sys

input = sys.stdin.readline

array = ['Never gonna give you up',
         'Never gonna let you down',
         'Never gonna run around and desert you',
         'Never gonna make you cry',
         'Never gonna say goodbye',
         'Never gonna tell a lie and hurt you',
         'Never gonna stop']

n = int(input())

flag = False

for i in range(n):
    s = input().rstrip()
    
    if s not in array:
        flag = True
        break
    
if flag:
    print('Yes')
else:
    print('No')