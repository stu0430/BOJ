array = [0] * 21
idx = 0

numbers = list(map(int, input().split()))
for i in range(1, 21):
    array[i] = numbers[i - 1]
    if array[i] == 20:
        idx = i

score = 0
if idx == 1:
    score = array[1] + array[2] + array[20]
elif idx == 20:
    score = array[1] + array[19] + array[20]
else:
    score = array[idx - 1] + array[idx] + array[idx + 1]

if score <= 31:
    print('Bob')
else:
    print('Alice')