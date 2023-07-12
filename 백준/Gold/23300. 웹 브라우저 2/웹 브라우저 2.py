import sys
from collections import deque

input = sys.stdin.readline

n, q = map(int, input().split())

p = 0
b, f = deque(), deque()

for i in range(q):
    w = input().rstrip()

    if w[0] == 'A':
        f = deque()

        if p != 0:
            b.append(p)

        p = int(list(w.split())[1])

    elif w == 'B':
        if b:
            f.appendleft(p)
            p = b[-1]
            b.pop()

    elif w == 'F':
        if f:
            b.append(p)
            p = f[0]
            f.popleft()

    elif w == 'C':
        s = []

        while b:
            if not s:
                s.append(b.pop())
            else:
                tmp = b.pop()

                if s[-1] != tmp:
                    s.append(tmp)

        while s:
            b.append(s.pop())

print(p)

if b:
    b.reverse()
    print(*b)
else:
    print(-1)

if f:
    print(*f)
else:
    print(-1)