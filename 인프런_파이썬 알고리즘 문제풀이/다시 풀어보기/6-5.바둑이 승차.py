import sys
sys.stdin=open('input.txt','r')

'''
259 5
81
58
42
33
61


259를 넘지 않으면서 가져갈수있는 최대의 무게는?

#1.그리디로 못푼다.완전탐색하면서 하나하나 확인해야함
#2.뽑고 가고, 안뽑고 가고, 
#3.만약에 L==N:까지 오면, 그때 total을 비교해서 갱신한다
'''
def dfs(L,total,tsum):
    global res
    #어떤 레벨까지 갔는데, 그 합+(앞으로 남은 무게)를 더했는데(현상태에서 최대가됨)
    #이미 구한 res보다 작다면? 갈필요도 없음, 여기서는 다 구해도 res보다 어차피 작을테니까
    if total + (sum(w)-tsum)<res:
        return
    if total>C:
        return
    if L==N:
        if total<=C:
            if total>res:
                res=total

    else:
        dfs(L+1,total+w[L],tsum+w[L])
        dfs(L+1,total,tsum+w[L])

if __name__ == '__main__':
    C,N=map(int,input().split())
    w=[]
    for _ in range(N):
        w.append(int(input()))
    res=0
    dfs(0,0,0)
    print(res)