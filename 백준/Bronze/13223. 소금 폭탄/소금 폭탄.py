ch,cm, cs = map(int, input().split(':'))
sh, sm, ss = map(int, input().split(':'))

sec = ((sh * 3600) + (sm * 60) + ss) - ((ch * 3600) + (cm * 60) + cs)

if sec <= 0:
    sec += 24 * 3600

h = sec // 3600
m = (sec % 3600) // 60
s = sec % 60

print(f'{h:02d}:{m:02d}:{s:02d}')