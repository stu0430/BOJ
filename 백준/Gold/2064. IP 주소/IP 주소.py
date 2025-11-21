import sys

input = sys.stdin.readline

n = int(input())
ip = [list(map(int, input().split('.'))) for _ in range(n)]

ipNetwork = [0] * 4
netWorkMask = [0] * 4

for byte in range(4):
    for bit in range(8):
        defaultBit = (ip[0][byte] >> (8 - 1 - bit)) & 1
        for i in range(1, n):
            if defaultBit ^ ((ip[i][byte] >> (8 - 1 - bit)) & 1):
                print(".".join(map(str, ipNetwork)))
                print(".".join(map(str, netWorkMask)))
                exit()
        ipNetwork[byte] |= (defaultBit << (8 - 1 - bit))
        netWorkMask[byte] |= 1 << (8 - 1 - bit)

print(".".join(map(str, ipNetwork)))
print(".".join(map(str, netWorkMask)))