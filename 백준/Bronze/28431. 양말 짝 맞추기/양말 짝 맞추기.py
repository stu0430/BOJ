numbers = set()

for _ in range(5):
    num = int(input())
    
    if num in numbers:
        numbers.remove(num)
    else:
        numbers.add(num)

for num in numbers:
    print(num)