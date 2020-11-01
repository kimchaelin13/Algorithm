import sys
sys.stdin = open("input.txt", "r")
# #D6 1267 작업순서
#
for t in range(1,3):
    v,e=map(int,input().split())
    graph=[[] for _ in range(v+1)]
    visited = [ False for _ in range(v+1)]
    temp_list= list(map(int,input().split()))

    #그래프 완성하기
    for i in range(0,len(temp_list),2):
        a=temp_list[i]
        b=temp_list[i+1]
        graph[b].append(a)
    #print(graph)

    result='' #결과값
    count=v
    while count:
        for i in range(1,len(graph)):
            #현재 노드가 수행되지 않았다면
            if visited[i] == False:

                # 선행노드를 확인한다.
                #for-else는 for문에서 BREAK가 발생하지 않았을 경우의 동작을 else에 적어주는 것임임
               for j in graph[i]:
                    #선행노드가 아직 수행되지 않았다면
                    if visited[j]==False:
                        break
               else:
                    #선행노드가 모두 수행되었다면
                    #현재노드를 수행노드로 바꾸고, 결과에 추가한다.
                    #노드가 수행되었으므로 cnt를 감소시킨다
                    visited[i]=True
                    result+=str(i)+' '
                    count-=1
    print('#{} {}'.format(t,result))

'''
원래 1 2
1번 노드의 리스트에 2 씀(1-2가 연결되어있다)
근데 이문제는 1 2 면, (2에 가려면 1을 방문하고 와야함)
반대로 적음 2번 노드 리스트에 1을 적어줌 맞나?ㅋ ㅁㄹ,,그다음어떻게하지?,,,,
'''
for tc in range(1,11):
    v,e=map(int,input().split())
    graph=[[0]*(v+1) for _ in range(v+1)]
    visited=[0 for _ in range(v+1)]
    temp=list(map(int,input().split()))


    # #두개씩 짝이니까, 2개씩 읽음,
    for i in range(0,len(temp),2):
        a=temp[i]
        b=temp[i+1]
        graph[b].append(a)

    result=''
    cnt=v #작업순서니까 끝까지

    while cnt: #모든 노드 다 방문
        for i in range(1,len(graph)):
            #지금 노드 아직 방문안찍혀있으면
            if visited[i]==0:
                #선행노드 확인한다
               for j in graph[i]:
                   #선행노드 아직 수행되지 않았으면
                    if visited[j]==0:
                        break
               else:
                   #선행노드 모두 수행되엇으면??
                    visited[i]=1
                    result+=str(i)+" "
                    cnt -= 1
    print('#{} {}'.format(tc,result))

