while True:
    n = int(input())

    if n == 0:
        break

    d = input().split()

    count = 0

    for i in range(0, len(d) - 3):
        if int(''.join(d[i:i + 4])) == 2020:
            count += 1
    
    print(count)