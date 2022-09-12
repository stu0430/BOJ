import sys

input = sys.stdin.readline

n = int(input())
players = []

for i in range(n):
    dice = list(map(int, input().split()))
    
    a = dice[0]
    b = dice[1]
    c = dice[2]
    
    if a == b == c:
        prize = 10000 + (a * 1000)
        
    elif a == c or a == b or b == c:
        if a == c or a == b:
            prize = 1000 + (a * 100)
            
        elif b == c:
            prize = 1000 + (b * 100)
            
    else:
        prize = max(dice) * 100
    players.append(prize)
    
print(max(players))