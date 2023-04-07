import sys

input = sys.stdin.readline

array = []

while True:
    s = input().rstrip()
    
    if s == '고무오리 디버깅 시작':
        continue
        
    elif s == '문제':
        array.append(s)
        
    elif s == '고무오리':
        if array:
            array.pop()
            
        else:
            array.append(s)
            array.append(s)
            
    elif s == '고무오리 디버깅 끝':
        break
    
if array:
    print('힝구')
    
else:
    print('고무오리야 사랑해')