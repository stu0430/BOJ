import sys

input = sys.stdin.readline

def binary_search(array, target, start, end):
    while start <= end:
        mid = (start + end) // 2
        if array[mid] == target:
            return mid
        elif array[mid] > target:
            end = mid - 1
        else:
            start = mid + 1
    return None

t = int(input())

for i in range(t):
    n = int(input())
    note_1 = list(map(int, input().split()))
    
    note_1.sort()
    
    m = int(input())
    note_2 = list(map(int, input().split()))
    
    for j in note_2:
        x = binary_search(note_1, j, 0, n - 1)
        if x != None:
            print('1')
        else:
            print('0')