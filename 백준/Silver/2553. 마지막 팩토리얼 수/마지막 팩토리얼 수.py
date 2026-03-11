import math  

n = int(input())  
facto = str(math.factorial(n))  

for i in range(len(facto)-1, -1, -1):  
    if facto[i] != '0':  
        print(facto[i])  
        break