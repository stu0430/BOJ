import sys

input = sys.stdin.readline

n  = int(input())

def recursion(s, l, r):
    global count
    count += 1
    if l >= r:
        return 1
    elif s[l] != s[r]:
        return 0
    else:
        return recursion(s, l + 1, r - 1)

def isPalindrome(s):
    return recursion(s, 0, len(s) - 1)

for i in range(n):
    count = 0
    print(isPalindrome(input().rstrip()), count)