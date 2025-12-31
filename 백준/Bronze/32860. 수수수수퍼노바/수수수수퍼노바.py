n, m = map(int, input().split())

if m <= 26:
    suffix = chr(ord('A') + m - 1)
else:
    q, r = divmod(m - 27, 26)
    suffix = chr(ord('a') + q) + chr(ord('a') + r)

print(f'SN {n}{suffix}')