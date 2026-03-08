n = int(input())
players = {}

for _ in range(n):
    name = input().rstrip()
    
    if name not in players:
        players[name] = 1
    else:
        players[name] += 1

for _ in range(n - 1):
    name = input().rstrip()
        
    if name in players:
        players[name] += 1

for name, count in players.items():
    if count % 2 == 1:
        print(name)
        break