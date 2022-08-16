import sys
import copy
word = sys.stdin.readline().rstrip()
new_word = copy.deepcopy(word)
new_word = new_word[::-1]
if word == new_word:
    print('1')
else:
    print('0')