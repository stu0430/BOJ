n = int(input())
a = list(map(int, input().split()))
b, c = map(int, input().split())

result = 0
for a_i in a:
    cnt = 1
    a_i -= b
    
    if a_i > 0:
        cnt += (a_i + c - 1) // c
        
    result += cnt

print(result)