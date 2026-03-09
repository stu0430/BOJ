n = int(input())

array = [0 for _ in range(n * 2)]
result = 0
sticker = 0

for i in map(int, input().split()):
    if not array[i]:
        sticker += 1
        result = max(sticker, result)
        array[i] = 1
        
    else:
        sticker -= 1

print(result)