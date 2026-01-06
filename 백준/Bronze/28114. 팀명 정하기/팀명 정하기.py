team = []
for _ in range(3):
    p, y, s = input().split()
    team.append((int(p), int(y), s))

years = sorted(member[1] % 100 for member in team)
print(f'{years[0]:02d}{years[1]:02d}{years[2]:02d}')

team_sorted = sorted(team, key=lambda x: -x[0])
print(''.join(member[2][0] for member in team_sorted))