import sys
t=int(sys.stdin.readline().strip())
arr=[]
for _ in range(t):
    n=int(sys.stdin.readline().strip())
    arr=[]
    for _ in range(n):
        arr.append(int(sys.stdin.readline().strip()))
    print(f"majority winner {arr.index(max(arr))+1}" if arr.count(max(arr))==1 and max(arr)>sum(arr)/2 else f"minority winner {arr.index(max(arr))+1}" if arr.count(max(arr))==1 else "no winner")