import sys
grades = {
    'A+': 4.5,
    'A0': 4.0,
    'B+': 3.5,
    'B0': 3.0,
    'C+': 2.5,
    'C0': 2.0,
    'D+': 1.5,
    'D0': 1.0,
    'F' : 0.0,
    }
sum = 0
x = 0
for i in range(20):
    subject, hakjum, grade = map(str,sys.stdin.readline().rstrip().split())
    hakjum = float(hakjum)
    if grade != 'P':
        sum += hakjum * grades[grade]
        x += hakjum
    else:
        pass
print(round(sum/x,6))