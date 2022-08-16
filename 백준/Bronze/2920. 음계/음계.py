number = list(map(int, input().split()))
lst = [i % 8 for i in number]
if lst == [1,2,3,4,5,6,7,0]:
    print('ascending')
elif lst == [0,7,6,5,4,3,2,1]:
    print('descending')
else:
    print('mixed')