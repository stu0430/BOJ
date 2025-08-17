n = int(input())
s = input().split()

result = set()
for i in range(n):
    result.add(s[i][0])
    
print(1 if len(result) == 1 else 0)