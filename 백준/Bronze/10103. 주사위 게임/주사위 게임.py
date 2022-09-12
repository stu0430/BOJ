import sys

input = sys.stdin.readline

dice1,dice2 = 100, 100

n = int(input())

for i in range(n):
    a, b = map(int, input().split())
    if a > b:
        dice2 -= a
    elif a < b: 
        dice1 -= b

print(dice1, dice2, sep='\n')