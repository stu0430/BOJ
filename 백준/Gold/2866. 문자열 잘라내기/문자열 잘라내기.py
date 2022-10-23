import sys

input = sys.stdin.readline

r, c = map(int, input().split())
array = [list(input().rstrip()) for i in range(r)]

start = 1
end = r - 1

while start <= end:
    mid = (start + end) // 2
    word_set = set()
    for j in range(c):
        word = ''
        for i in range(mid, r):
            word += array[i][j]
        word_set.add(word)
        
    if len(word_set) != c:
        end = mid - 1
        
    else:
        start = mid + 1

print(end)