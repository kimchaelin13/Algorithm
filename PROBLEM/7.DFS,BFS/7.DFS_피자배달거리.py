import sys
sys.stdin = open("input.txt", "r")


def DFS(L,s):
    global res
    if L == m:
        #거리
        sum=0
        for j in range(len(hs)):
            x1=hs[j][0]
            y2=hs[j][1]

    else:
        for i in range(s,len(pz)):
            cb[L]=i
            DFS(L+1,i+1)







if __name__=='__main__':
    n,m=map(int,input().split())
    board=[list(map(int,input().split())) for _ in range(n)]
    hs=[]
    pz=[]
    cb=[0]*m #combination, m개가 살아남으니까! 조합의 경우의 수를 저장하는 리스트
    res=987654321
    for i in range(n):
        for j in range(n):
            if board[i][j]==1:
                hs.append((i,j))
            elif board[i][j]==2:
                #pz의 길이가 6이면 0부터 5까지 for문이 돌면서
                #그 중에 4개를 뽑아내는거임
                pz.append((i,j))
    DFS(0,0)
