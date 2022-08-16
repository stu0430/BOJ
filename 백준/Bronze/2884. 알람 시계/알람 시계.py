H, M = map(int, input().split())
if M > 45:
    print(H, M-45)
elif M == 45:
    print(H, 0)
elif M < 45:
    if H>=1:
        print(H-1, M+15)
    else:
        print(23, M+15)