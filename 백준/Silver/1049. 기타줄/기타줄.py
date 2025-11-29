n, m = map(int, input().split())
six_prices = []
one_prices = []

for _ in range(m):
    six, one = map(int, input().split())
    six_prices.append(six)
    one_prices.append(one)

six_min = min(six_prices)
one_min = min(one_prices)

only_six = ((n + 5) // 6) * six_min
only_one = n * one_min
mixed = (n // 6) * six_min + (n % 6) * one_min

print(min(only_six, only_one, mixed))