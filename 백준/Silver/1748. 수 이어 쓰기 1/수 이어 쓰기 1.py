N = input()
n_len = len(N) - 1

ans = 0
for i in range(n_len):
    ans += 9 * (10 ** i) * (i + 1)

ans += ((int(N) - (10 ** n_len)) + 1) * (n_len + 1)
print(ans)