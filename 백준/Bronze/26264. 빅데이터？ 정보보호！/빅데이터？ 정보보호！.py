import sys

input = sys.stdin.readline

n = int(input())

array = [['security', 0], ['bigdata', 0]]

s = input().rstrip()

for i in array:
    i[1] = s.count(i[0])
    
if array[0][1] == array[1][1]:
    print('bigdata? security!')
    exit()
    
result = max(array, key= lambda x: x[1])[0]

if result == 'security':
    print('security!')
else:
    print('bigdata?')