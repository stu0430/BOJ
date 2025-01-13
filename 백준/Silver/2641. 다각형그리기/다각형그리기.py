import sys
from collections import deque

input = sys.stdin.readline

def convert(x):
    return (x + 2) % 4 if x != 2 else 4

n = int(input())
array = deque(map(int, input().split()))

revese = deque(map(convert, array))
revese.reverse()

count = 0
result = []

for _ in range(int(input())):
    data = deque(map(int, input().split()))
    data_2 = data.copy()

    for _ in range(n):
        if array == data_2 or revese == data_2:
            count += 1
            result.append(data)
            
        data_2.rotate(1)

print(count)

for i in result:
    print(*i)