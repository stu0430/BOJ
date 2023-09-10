import sys
import heapq

input = sys.stdin.readline

n, k = map(int, input().split())
array = list(map(int, input().split()))

prefix_sum = [0] * (n + 1)
for i in range(n):
    prefix_sum[i + 1] = prefix_sum[i] + array[i]

queue = []
for i in range(n):
    heapq.heappush(queue, (-prefix_sum[i + 1], i + 1))

result = 0
for _ in range(k):
    score, idx = heapq.heappop(queue)
    result -= score 
            
print(result)