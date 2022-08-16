N = int(input())
m = 1
def pactorial(i):
    global m, N
    if i == N:
        return m
    m *= (i+1)
    return pactorial(i+1)
print(pactorial(0))
