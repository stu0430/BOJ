n, k = map(int, input().split())
g = list(map(int, input().split()))

cutoffs = [4, 11, 23, 40, 60, 77, 89, 96]
result = []

for score in g:
    percentage = score * 100 // n
    grade = 9
    
    for i, cutoff in enumerate(cutoffs):
        if percentage <= cutoff:
            grade = i + 1
            break
        
    result.append(grade)

print(*result)