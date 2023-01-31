import sys
from math import factorial

n = sys.stdin.readlines()

for line in n:
    x = ""        
    
    for i in reversed(str(factorial(int(line.rstrip())))):
        if i != "0":
            x = i
            break
            
    print(f"{str(line.rstrip()).rjust(5)} -> {x}")