numbers = list(map(int, input().split()))
target = [1, 2, 3, 4, 5]

while numbers != target:
    for i in range(4):
        if numbers[i] > numbers[i+1]:
            numbers[i], numbers[i+1] = numbers[i+1], numbers[i]
            print(' '.join(map(str, numbers)))