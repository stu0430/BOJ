import sys

input = sys.stdin.readline

n, m = map(int, input().split())

white = []
blue = []
students = []

while True:
    grade, name = map(str, input().rstrip().split())
    if grade == '0' and name == '0':
        break
    else:
        grade = int(grade)
        students.append(grade)
        if students.count(grade) >= m + 1:
            pass
        else:
            if grade % 2 == 0:
                white.append((grade, name))
            else:
                blue.append((grade, name))
                
blue = sorted(blue, key=lambda x:(x[0], len(x[1]), x[1]))
white = sorted(white, key=lambda x:(x[0], len(x[1]), x[1]))

for i in blue:
    print(i[0], i[1])
    
for j in white:
    print(j[0], j[1])