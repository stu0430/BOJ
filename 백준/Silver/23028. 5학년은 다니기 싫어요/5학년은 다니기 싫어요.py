n, a, b = map(int, input().split())
semester = [list(map(int, input().split())) for _ in range(10)]

if b >= 130 and a >= 66:
    print('Nice')
    
else:
    for i in range(8 - n):
        major = semester[i][0]
        a += major * 3
        b += major * 3
        
        remain_class = 6 - major
        
        non_major = min(remain_class, semester[i][1])
        b += non_major * 3
    
    if b >= 130 and a >= 66:
        print('Nice')
        
    else:
        print('Nae ga wae')