while True:
    num = int(input())
    if num == 0:
        break
    else:
        num = str(num)
        if num == num[::-1]:
            print('yes')
        else:
            print('no')