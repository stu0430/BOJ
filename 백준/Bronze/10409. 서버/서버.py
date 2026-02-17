n, t = map(int, input().split())
jobs = list(map(int, input().split()))

for i, job in enumerate(jobs):
    if t < job:
        print(i)
        break
    
    t -= job
    
else:
    print(n)