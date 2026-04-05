import sys

input = sys.stdin.readline

def find(p, x):
    if x != p[x]:
        p[x] = find(p, p[x])
    return p[x]

def union(p, a, b, true):
    a_root = find(p, a)
    b_root = find(p, b)

    if a_root in true and b_root in true:
        return
    
    if a_root in true:
        p[b_root] = a_root
        
    elif b_root in true:
        p[a_root] = b_root
        
    else:
        if a_root < b_root:
            p[b_root] = a_root
        else:
            p[a_root] = b_root

n, m = map(int, input().split())
true = list(map(int, input().split()))[1:]
parties = []
p = list(range(n + 1))

for _ in range(m):
    party = list(map(int, input().split()))[1:]
    
    for i in range(len(party) - 1):
        union(p, party[i], party[i + 1], true)
        
    parties.append(party)

result = 0
for party in parties:
    if not any(find(p, person) in true for person in party):
        result += 1

print(result)