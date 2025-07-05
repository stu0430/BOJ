n = int(input())
tips = sorted([int(input()) for _ in range(n)], reverse=True)
print(sum(max(0, tip - i) for i, tip in enumerate(tips)))