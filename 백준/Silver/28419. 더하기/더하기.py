n = int(input())
a = list(map(int, input().split()))

odd = sum(a[i] for i in range(n) if i % 2 == 0)
even = sum(a[i] for i in range(n) if i % 2 == 1)

if odd == even:
    print(0)
    
elif even < odd:
    if n <= 3:
        print(-1)
    else:
        print(odd - even)
else:
    print(even - odd)