lst = []
for i in range(5):
    score = list(map(int, input().split()))
    fn_score = sum(score)
    lst.append(fn_score)
wn_score = max(lst)
winner = lst.index(wn_score) + 1
print(winner, wn_score)