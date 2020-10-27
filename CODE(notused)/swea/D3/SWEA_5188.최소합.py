import sys
sys.stdin=open('input.txt','r')

'''
3
3
1 2 3
2 3 4
3 4 5
4
2 4 1 3
1 1 7 1
9 1 7 10
5 7 2 4
5
6 7 1 10 2
10 2 7 5 9
9 3 2 9 6
1 6 8 2 9
8 3 8 2 1



#1.입력받고, dfs로 풀건데 dx=[0,1], dy=[1,0] 
#2.종료까지 왔을때 sum을 비교한다
#3.갖고다니는 썸이 기존썸보다 더 작을때 답을 갱신한다
'''

di=[0,1]
dj=[1,0]
def min_route(i,j,total):
    global res
    #시간초과나서 cutedge
    #만약에 지금 갖고다니는 total이 기존에 저장했던 res를 이미 초과했다면? return
    if total>res:
        return
    if i==N-1 and j==N-1:
        if res>total:
            res=total

    else:
        for d in range(2):
            ni=i+di[d]
            nj=j+dj[d]
            if 0<=ni<N and 0<=nj<N:
                min_route(ni,nj,total+arr[ni][nj])

for tc in range(1,int(input())+1):
    N=int(input())
    arr=[list(map(int,input().split())) for _ in range(N)]
    res=987654321
    min_route(0,0,arr[0][0])
    print('#{} {}'.format(tc,res))

