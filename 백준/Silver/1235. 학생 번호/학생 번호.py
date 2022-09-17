import sys

input = sys.stdin.readline

n = int(input())

count = 1
students = []

for i in range(n):
    students.append(int(input()))
    
while True:
    lst = []
    
    for j in range(n):
        if (students[j] % (10 ** count) in lst):
            count += 1
            break
        else: 
            lst.append(students[j] % (10 ** count))
            
    if len(lst) == len(students): 
        break
        
print(count)