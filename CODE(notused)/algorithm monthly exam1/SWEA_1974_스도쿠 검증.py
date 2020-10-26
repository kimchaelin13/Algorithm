import sys
sys.stdin = open("input.txt", "r")
'''
와~~~내힘으로 풀었다~~~~
'''
for tc in range(1,int(input())+1):
    arr=[list(map(int,input().split())) for _ in range(9)]
    result=1
    #가로
    for r in range(9):
        row_s = set()
        for c in range(9):
            row_s.add(arr[r][c])
        if len(row_s) != 9:
            result=0
            break

    #세로
    for r in range(9):
        col_s=set()
        for c in range(9):
            col_s.add(arr[c][r])
        if len(col_s) != 9:
            result=0
            break
    #3*3
    for r in range(0,9,3):
        for c in range(0,9,3):
            cross_s = set()
            for m in range(3):
                cross_s.update(arr[r+m][c:c+3])
            if len(cross_s) != 9:
                result=0
                break
    print('#{} {}'.format(tc,result))

