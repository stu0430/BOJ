def BottlesofBeer(cnt):
    if cnt == 0:
        return 'no more bottles'
    elif cnt == 1:
        return '1 bottle'
    else:
        return str(cnt) + ' bottles'

n = int(input())

for i in range(n, 0, -1):
    print(f'{BottlesofBeer(i)} of beer on the wall, {BottlesofBeer(i)} of beer.')
    print(f'Take one down and pass it around, {BottlesofBeer(i - 1)} of beer on the wall.')
    print()

print('No more bottles of beer on the wall, no more bottles of beer.')
print(f'Go to the store and buy some more, {BottlesofBeer(n)} of beer on the wall.')