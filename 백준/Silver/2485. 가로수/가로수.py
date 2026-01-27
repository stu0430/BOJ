import sys
import math 

input = sys.stdin.readline

n = int(input()) 

array = [] 
t = set() 

result = 0 

for i in range(n): 
    array.append(int(input())) 

    if i != 0: 
        t.add(array[i] - array[i - 1]) 

min_t = math.gcd(*t)

for i in range(1, n): 
    if min_t == array[i] - array[i - 1]: 
        continue 

    else: 
        result += ((array[i] - array[i - 1]) // min_t) - 1 

print(result)