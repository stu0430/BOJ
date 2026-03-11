import sys

input = sys.stdin.readline

n = int(input())
array = [tuple(map(int, input().split())) for _ in range(n)]

dp = [{} for _ in range(n)]
a0, b0 = array[0]
dp[0][a0] = 1
dp[0][b0] = 1

max_count = 1
grade = min(a0, b0)

for i in range(1, n):
    for ab in array[i]:
        prev_count = dp[i - 1].get(ab, 0)
        dp[i][ab] = prev_count + 1
        
        if dp[i][ab] > max_count:
            max_count = dp[i][ab]
            grade = ab
            
        elif dp[i][ab] == max_count:
            grade = min(grade, ab)

print(max_count, grade)