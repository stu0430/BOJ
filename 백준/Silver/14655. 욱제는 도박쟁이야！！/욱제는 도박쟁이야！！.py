n = int(input())

f = list(map(int, input().split()))
s = list(map(int, input().split()))

sf = sum(map(abs, f))
ss = sum(map(abs, s))
    
print(sf + ss)