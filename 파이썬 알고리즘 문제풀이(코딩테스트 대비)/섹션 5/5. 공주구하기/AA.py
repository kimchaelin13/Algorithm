

import sys
from collections import deque
sys.stdin=open("input.txt","r")
n,k=map(int,input().split())

dq=list(range(1,n+1)) #1부터 8까지 list화됨, 이건 아직 리스트

#k-1개는 팝해서 뒤로 append하고, 계속하는데 k번째는 그냥 pop만시킴
#큐가 비면 멈출거임
while dq:
    for _ in range(k-1):
        #처음에는 앞에 자료 1이 pop되고 cur이라는 변수에 들어가고
        cur=dq.popleft()
        #이걸 다시 뒤로 가서 append함. 이게 회전하는거임
        #원형으로 앉아있으니까 그 효과를 낼려고 뒤로 가는거임
        dq.append(cur)
    #k번째 사람, q에서 사라지게 됨
    dq.popleft()
    if len(dq)==1:
        print(dq[0])
        dq.popleft()


