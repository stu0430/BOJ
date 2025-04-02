t = int(input())
n = list(map(int, input().split()))

d = [0] * 80001
answer = 0

for i in range(80001):
    if i % 3 == 0 or i % 7 == 0:
        answer += i
    d[i] = answer


for j in n:
    print(d[j])