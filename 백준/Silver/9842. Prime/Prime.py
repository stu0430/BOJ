def prime_check(x):
    for i in range(2,int(x**0.5)+1):
        if x % i == 0:
            return False
    return True

lst = [i for i in range(2,150000) if prime_check(i)]
print(lst[int(input())-1])