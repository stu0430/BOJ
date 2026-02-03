from itertools import permutations

n = int(input())
k = int(input())
cards = [input() for _ in range(n)]

result = {''.join(p) for p in permutations(cards, k)}

print(len(result))