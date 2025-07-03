n = int(input())

for _ in range(n):
    sentence = input().lower()

    miss = ''

    for alpha in range(ord('a'), ord('z') + 1):
        if chr(alpha) not in sentence:
            miss += chr(alpha)

    if miss == '':
        print('pangram')
    else:
        print(f'missing {miss}')