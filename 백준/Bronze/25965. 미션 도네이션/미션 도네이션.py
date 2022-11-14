import sys

input = sys.stdin.readline

n = int(input())

for i in range(n):
    donation = 0
    missions = []
    
    m = int(input())
    
    for j in range(m):
        mission = tuple(map(int, input().split()))
        missions.append(mission)
    
    K, D, A = map(int, input().split())
    
    for k in missions:
        sum = K * k[0] - D * k[1] + A * k[2]
        
        if sum > 0:
            donation += sum
            
    print(donation)