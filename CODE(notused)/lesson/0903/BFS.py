'''
인접리스트 좋은점- 인접행렬은 비어있는 것도 무조건 돌아야하는데 리스트는
ㅇ가지고 있는것만 돌면되서 ㄱㅊ
'''

def BFS(a):
    queue=[]
    queue.append(a)

    visited[a]=1 #시작점 방문 체크

    #비어있지 않을때까지 계속돌거야
    while len(queue)>0:
        curr=queue.pop(0)
        print(curr,end=" ")

        for i in adj_list[curr]:
            if not visited[i]:
                queue.append(i)
                visited[i]=1



V,E=map(int,input().split())

adj_list= [[] for _ in range(V+1)]

for i in range(E):
    st,ed=map(int,input().split())
    adj_list[st].append(ed)
    adj_list[ed].append(st)
visited=[0]*(V+1)