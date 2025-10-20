code_map = {
    '**** ** ** ****': '0',
    '  *  *  *  *  *': '1',
    '***  *****  ***': '2',
    '***  ****  ****': '3',
    '* ** ****  *  *': '4',
    '****  ***  ****': '5',
    '****  **** ****': '6',
    '***  *  *  *  *': '7',
    '**** ***** ****': '8',
    '**** ****  ****': '9'
}

codes = [input() for _ in range(5)]

digits = []
for col in range(0, len(codes[0]), 4):
    pattern = ''.join(code[col:col+3] for code in codes)
    
    if pattern in code_map:
        digits.append(code_map[pattern])
    else:
        print('BOOM!!')
        exit()

print('BEER!!' if int(''.join(digits)) % 6 == 0 else 'BOOM!!')