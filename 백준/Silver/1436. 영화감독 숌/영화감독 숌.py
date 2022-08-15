n = int(input())
lst = [i for i in range(1,(n*1000)+1) if '666' in str(i)]
print(lst[n-1])