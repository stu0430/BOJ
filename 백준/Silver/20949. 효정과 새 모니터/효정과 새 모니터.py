import math

n = int(input())
m = []

for i in range(n):
    w, h = map(int, input().split())
    ppi = math.sqrt(w**2 + h**2) / 77
    m.append((i + 1, ppi))

m.sort(key=lambda x: (-x[1], x[0]))

for m_id, _ in m:
    print(m_id)