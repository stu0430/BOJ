import sys

input = sys.stdin.readline

n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))

result = []
while a and b:
    tmp1, tmp2 = max(a), max(b)
    idx1, idx2 = a.index(tmp1), b.index(tmp2)
    
    if tmp1 == tmp2:
        result.append(tmp1)
        a = a[idx1 + 1:]
        b = b[idx2 + 1:]
        
    elif tmp1 > tmp2:
        a.pop(idx1)
        
    else:
        b.pop(idx2)

print(len(result))
print(*result) if result else None