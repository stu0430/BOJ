num = list(map(int, input().split()))
gum = 0
for i in num:
    gum += i**2
print(gum%10)