for i in range(3):
    n = list(map(int, input().split()))
    if n.count(1) == 1:
        print('C')
    elif n.count(1) == 2:
        print('B')
    elif n.count(1) == 3:
        print("A")
    elif n.count(1) == 4:
        print('E')
    elif n.count(1) == 0:
        print('D')