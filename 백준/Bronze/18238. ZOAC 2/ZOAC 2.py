s = 'A' + input()
count = 0

for i in range(len(s) - 1):
    diff = abs(ord(s[i + 1]) - ord(s[i]))
    count += min(diff, 26 - diff)
    
print(count)