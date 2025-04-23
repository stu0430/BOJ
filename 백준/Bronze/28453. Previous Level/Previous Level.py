n = int(input())
m = list(map(int, input().split()))

for i in m:
    if i == 300:
        print(1, end=' ')
        
    elif 275 <= i < 300:
        print(2, end=' ')
        
    elif 250 <= i < 275:
        print(3, end=' ')
        
    elif i < 250:
        print(4, end=' ')