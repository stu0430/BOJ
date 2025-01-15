import sys

input = sys.stdin.readline

mw, mb = map(int, input().split())
tw, tb = map(int, input().split())
pw, pb = map(int, input().split())

array1, array2 = [mw, tb, pw], [mb, tw, pb]

array1.sort()
array2.sort()

result = [array1[0], array2[0]]
result.sort()

if result[1] - result[0] not in [0, 1]:
    print(result[0] * 2 + 1)

else:  
    print(result[0] + result[1])