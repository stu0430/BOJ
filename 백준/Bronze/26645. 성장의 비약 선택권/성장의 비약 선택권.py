import sys

input = sys.stdin.readline

n = int(input())

dic = {'1' : n, '2' : n, '3' : n, '4' : n}

a_c, b_c, c_c = 8, 4, 2

while True:
    if a_c == 0 or dic['1'] >= 210:
        break

    dic['1'] += 1
    a_c -= 1
    
while True:
    if b_c == 0 or dic['2'] >= 220:    
        break
        
    dic['2'] += 1
    b_c -= 1
        
while True:
    if c_c == 0 or dic['3'] >= 230:
        break

    dic['3'] += 1
    c_c -= 1
     
if 200 <= n <= 239:
    dic['4'] += 1
    
dic = sorted(dic.items(), key=lambda x: (x[1], x[0]))

print(dic[-1][0])