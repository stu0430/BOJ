import sys

input = sys.stdin.readline

n = int(input())
persons = []

for i in range(n):
    age, name = map(str, input().rstrip().split())
    persons.append([int(age), name])
    
persons = sorted(persons, key=lambda x: x[0])

for j in persons:
    print(j[0], j[1])