n = int(input())
c = list(map(int, input().split()))

max_val = 0
total_sum = 0

for i in c:
    total_sum += i
    
    if max_val < i:
        max_val = i

print(total_sum - max_val)