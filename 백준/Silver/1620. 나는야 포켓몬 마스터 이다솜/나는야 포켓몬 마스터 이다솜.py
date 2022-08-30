import sys

input = sys.stdin.readline

n, m = map(int, input().split())

dict = {}

for i in range(1, n+1):
    a = input().rstrip()
    dict[i] = a
    dict[a] = i

for j in range(m):
    quiz = input().rstrip()
    if quiz.isdecimal() == True:
        print(dict[int(quiz)])
    else:
        print(dict[quiz])