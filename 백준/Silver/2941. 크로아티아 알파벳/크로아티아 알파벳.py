croatian = ['c=', 'c-', 'dz=', 'd-', 'lj', 'nj', 's=', 'z=']
word = input()
count = 0
for i in croatian:
    if i in word:
        count += word.count(i)
        word = word.replace(i, '@')
count_2 = len(word) - word.count('@')
print(count + count_2)