import sys

input = sys.stdin.readline

s = input().rstrip()

max_n, sum_n = -1, 0

for i in s:
    if i == '[':
        sum_n += 3
        
    elif i == '{':
        sum_n += 2
        
    elif i == '(':
        sum_n += 1
        
    elif i == ')':
        sum_n -= 1
        
    elif i == '}':
        sum_n -= 2
        
    elif i == ']':
        sum_n -= 3
        
    elif '0' <= i <= '9':
        if sum_n > max_n:
            max_n = sum_n
            
print(max_n)