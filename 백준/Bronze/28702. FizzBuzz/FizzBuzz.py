array = list(input() for _ in range(3))

FizzBuzz = ['FizzBuzz', 'Fizz', 'Buzz']

for i, x in enumerate(array):
    if x not in FizzBuzz:
        result = int(x) + 3 - i
        break
    
if result % 15 == 0:
    print('FizzBuzz')
    
elif result % 3 == 0:
    print('Fizz')
    
elif result % 5 == 0:
    print('Buzz')
    
else:
    print(result)