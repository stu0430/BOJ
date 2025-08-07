n = int(input())
s = list(map(int, input().split()))

streak, result = 0,0

for i in s:
    if i == 0:
        streak = 0
        
    else:
        streak += 1
        result = max(result, streak)
        
print(result)