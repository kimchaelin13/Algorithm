import sys
sys.stdin = open("input2.txt", "r")

'''
DFS로 푸는 문제, 
방문체크는 할 필요가 없는것같다 원소가 다 다르다고 함
'''


#cnt는 이동거리를 세주는 변수임
di=[0,0,1,-1]
dj=[1,-1,0,0]
def DFS(i,j,start,cnt):

    global max_length, result

    if cnt>max_length:
        max_length=cnt
        result=start

    if cnt==max_length and start<result:
        result=start

    for d in range(4):
        ni=i+di[d]
        nj=j+dj[d]

        if 0<=ni<N and 0<=nj<N and rooms[ni][nj]==rooms[i][j]+1:
            DFS(ni,nj,start,cnt+1)



for tc in range(1,int(input())+1):
    N=int(input())
    rooms=[list(map(int,input().split())) for _ in range(N)]
    #print(rooms)
    max_length=0 #이거보다 길이를 세는 cnt가 커지면 그때의 cnt를 max_length에 할당
    result=rooms[0][0] #이렇게 하고 갱신
    #cnt=1로, 시작도 길이에 포함되니까
    for i in range(N):
        for j in range(N):
            DFS(i,j,rooms[i][j],1)
    print('#{} {} {}'.format(tc,result,max_length))

