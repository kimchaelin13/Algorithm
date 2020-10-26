
def DFS(v):
    work[v]=1 #노드방문을 했으니 작업했음을 표시
    for w in adj[v]: #해당 작업의 후행 작업순회
        if not work[w]: #해당작업을 하지 않았으면 수행
            DFS(w)
    stack.append(v) #스택에 v작업 담기

for tc in range(1,11):
    V,E=map(int,input().split())
    #인접리스트
    adj=[[] for _ in range(V+1)]
    work = [0]*(V+1) #일을 했는지 안했는지
    count = [0]*(V+1) #선행작업카운트

    stack=[]

    edge=list(map(int,input().split()))
    for i in range(0,E):
        st,ed=adj[i*2][i*2+1]
        adj[st].append(ed)
        count[ed]+=1 #선행작업 개수 증가

    for i in range(1,V+1):
        if count[i]==0:#선행작업이 없는 노드먼저 시작!!
            DFS(i)
    print('#{} {}'.format(tc,*stack[::-1]))
