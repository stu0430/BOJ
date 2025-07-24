data = input().split()

ms_moves = set(data[:2])
tk_moves = set(data[2:])

win_against = {'R': 'P', 'P': 'S', 'S': 'R'}

if len(ms_moves) == 1 and win_against[list(ms_moves)[0]] in tk_moves:
    print('TK')
    
elif len(tk_moves) == 1 and win_against[list(tk_moves)[0]] in ms_moves:
    print('MS')
    
else:
    print('?')