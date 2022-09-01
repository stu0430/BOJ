import sys

input = sys.stdin.readline

n = int(input())
lst = []
cnt = 0

if n == 1:
    print(0)
    exit()
    
else:
    for i in range(n):
        x = int(input())
        lst.append(x)
        
    y = lst[0]
    lst.pop(0)
    
    while True:
        if y <= max(lst):
            cnt += 1
            lst[lst.index(max(lst))] -= 1
            y += 1
        else:
            break
            
print(cnt)