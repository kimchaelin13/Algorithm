for tc in range(1,11):
    V,E=map(int,input().split())
    edges=list(map(int,input().split()))

    prev_arr=[[0]*(V+1) for _ in range(V+1)]

    order=[]

    work=[0]*(V+1)

    for i in range(0,len(edges),2):
        st,ed=edges[i],edges[i+1]
        prev_arr[ed][st]=1 #선행

    #선행작업이 하나도 없는 일은 미리 담아두자!
    #예제기준으로 4,8은 담아놓은 상태임
    for i in range(1,len(prev_arr)):
        if prev_arr[i].count(i) == 0:
            order.append(i)
            work[i]=1

    #작업을 할차례
    while len(order) != V:
        for i in range(1,V+1):
            #해당작업을 안했따면
            if work[i] == 0:
                #선행작업을 확인
                for j in range(1,V+1):
                    #선행작업이 있다면
                    if prev_arr[i][j] == 1:
                        #그거 안했어? 그러면 break
                        if work[j] == 0:
                            break
                #조기 브레이크 연결했어?그러면 일해
                else:
                    order.append(i)
                    work[i]=1


    print('#{}'.format(tc),end=" ")
    for i in order:
        print(i,end=" ")
    print()