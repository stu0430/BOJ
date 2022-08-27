import sys

input = sys.stdin.readline

word = input().rstrip()
new_word = []

for i in range(len(word)):
    if word[i].islower():
        new_word.append(word[i].upper())
    else:
        new_word.append(word[i].lower())
        
print(*new_word, sep='')