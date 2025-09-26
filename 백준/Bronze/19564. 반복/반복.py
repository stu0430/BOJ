s = str(input())
print(sum([1 for x in range(1, len(s)) if s[x] <= s[x-1]]) + 1)