s = input()

for char in s:
    ascii_code = ord(char)
    tmp = ascii_code // 100 + (ascii_code % 100) // 10 + ascii_code % 10
    
    print(char * tmp)