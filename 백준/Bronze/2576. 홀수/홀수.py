array = [num for num in [int(input()) for _ in range(7)] if num % 2 == 1]

if array:
    print(sum(array), min(array), sep='\n')
    
else:
    print(-1)