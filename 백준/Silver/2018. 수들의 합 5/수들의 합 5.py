n = int(input())
result = 1
start = 1
end = 1
current_sum = 1

while end != n:
    if current_sum == n:
        result += 1
        end += 1
        current_sum += end
        
    elif current_sum > n:
        current_sum -= start
        start += 1
        
    else:
        end += 1
        current_sum += end

print(result)