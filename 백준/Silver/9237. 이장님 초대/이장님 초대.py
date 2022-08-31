import sys

input = sys.stdin.readline

n = int(input())

tree = list(map(int, input().split()))
tree.sort(reverse=True)

arr = [0] * n

for i in range(n):
    arr[i] = i + 1 + tree[i]
    
print(max(arr) + 1)