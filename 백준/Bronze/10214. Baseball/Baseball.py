t = int(input())
Yonsei = 0
Korea  = 0
for j in range(t):
    for i in range(9):
        a, b = map(int, input().split())
        Yonsei += a
        Korea  += b
    if Yonsei > Korea:
        print('Yonsei')
    elif Yonsei < Korea:
        print('Korea')
    elif Yonsei == Korea:
        print('Draw')