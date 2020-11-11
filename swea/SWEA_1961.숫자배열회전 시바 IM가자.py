import sys
sys.stdin=open('input.txt','r')

'''
5 2
1 3 3 6 7
8 13 9 12 8
4 16 11 12 6
2 4 1 23 2
9 13 4 7 3

#1.배열을 먼저 입력받고
#2.2*2만 더해서 max값이 지금값보다 더 작으면 max값을 갱신해준다.
'''
for tc in range(1,int(input())+1):
    N,M=map(int,input().split())
    arr=[list(map(int,input().split())) for _ in range(N)]
    #print(arr)
    MAX=-9876543321
    for r in range(N-M+1):
        for c in range(N-M+1):
            temp,minus=0,0
            for m in range(M):
                temp += sum(arr[r+m][c:c+M])

                if m!=0 and m!=M-1:
                    minus += sum(arr[r+m][c+1:c+
    print('#{} {}'.format(tc,MAX))