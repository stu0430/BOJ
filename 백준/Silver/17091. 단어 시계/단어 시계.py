import sys

input = sys.stdin.readline

h = int(input())
m = int(input())

h_list = ['zero', 'one', 'two', 'three', 'four', 'five',
          'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'one']

m_list = ['o\' clock', 'one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine', 'ten', 'eleven', 'twelve', 'thirteen', 'fourteen', 'quarter', 'sixteen', 'seventeen',
          'eighteen', 'nineteen', 'twenty', 'twenty one', 'twenty two', 'twenty three', 'twenty four', 'twenty five', 'twenty six', 'twenty seven', 'twenty eight', 'twenty nine', 'half']

if m == 0:
    print(f'{h_list[h]} {m_list[m]}')
    
elif 1 <= m <= 30:
    if m == 1:
        print(f'{m_list[m]} minute past {h_list[h]}')
        
    elif m == 15 or m == 30:
        print(f'{m_list[m]} past {h_list[h]}')
        
    else:
        print(f'{m_list[m]} minutes past {h_list[h]}')
else:
    m = 60 - m
    
    if m == 1:
        print(f'{m_list[m]} minute to {h_list[h + 1]}')
        
    elif m == 15 or m == 30:
        print(f'{m_list[m]} to {h_list[h + 1]}')
        
    else:
        print(f'{m_list[m]} minutes to {h_list[h + 1]}')