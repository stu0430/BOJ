import sys

input = sys.stdin.readline

s = input().rstrip()
card = [s[i:i+3] for i in range(0, len(s)-2, 3)]

if len(set(card)) != len(card):
    print('GRESKA')
    
else:
    result = {'P': 13, 'K': 13, 'H': 13, 'T': 13}
    
    for c in card:
        result[c[0]] -= 1
        
    print(result['P'], result['K'], result['H'], result['T'])