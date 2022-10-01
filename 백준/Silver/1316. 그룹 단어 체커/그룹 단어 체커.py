import sys

input = sys.stdin.readline

n = int(input())

count = 0

for i in range(n):
    word = input().rstrip()
    for j in range(len(word) - 1):
        if word.find(word[j]) > word.find(word[j + 1]):
            count += 1
            break
            
print(n - count)