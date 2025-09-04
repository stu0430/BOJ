a = list(map(int, input().split()))
b = list(map(int, input().split()))
a_score, b_score = 0, 0
last_win = None

for a, b in zip(a, b):
    if a > b:
        a_score += 3
        last_win = 'A'
    elif a < b:
        b_score += 3
        last_win = 'B'
    else:
        a_score += 1
        b_score += 1

print(a_score, b_score)

if a_score == b_score:
    print('D' if last_win is None else last_win)
else:
    print('A' if a_score > b_score else 'B')