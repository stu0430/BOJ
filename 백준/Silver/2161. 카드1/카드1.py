n = int(input())
card = [i+1 for i in range(n)]
for i in range(n-1):
    print(card[0],end=' ')
    card = card[1:]
    x = card[0]
    del card[0]
    card.append(x)
print(card[0])