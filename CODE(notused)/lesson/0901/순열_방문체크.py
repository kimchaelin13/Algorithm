arr=[1,2,3]
N=3

sel=[0]*N
visited=[0]*N

def perm(idx):
    if idx==N:
        print(sel)
        return
    for i in range(N):
        # if visited[i] == True:
        #     continue
        if not visited[i]:
            sel[idx]=arr[i]
            visited[i]=1
            perm(idx+1)
            #다음꺼를 시도해야하기 때문에 다시 돌리기전에 아무일도없었다, 복구
            visited[i]=0

perm(0)