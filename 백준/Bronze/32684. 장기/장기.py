c = list(map(int, input().split()))
score_c = c[0] * 13 + c[1] * 7 + c[2] * 5 + c[3] * 3 + c[4] * 3 + c[5] * 2

e = list(map(int, input().split()))
score_e = e[0] * 13 + e[1] * 7 + e[2] * 5 + e[3] * 3 + e[4] * 3 + e[5] * 2 + 1.5

if score_c > score_e: 
    print('cocjr0208')
else: 
    print('ekwoo')