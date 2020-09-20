import sys
import heapq as hq #리스트가 힙의 자료구조처럼 저장이 됨
sys.stdin=open("input.txt","r")

a=[]
while True:
    n=int(input())
    if n==-1:
        break
    if n==0:
        #힙의 루트노드 뽑아야하는데,
        #힙의 자료가 없을수도있기때문에
        if len(a)==0:
            print(-1) #비어있으면 -
        #heappop이라는 함수가 a에서 루트노드를 pop해줌!
        else:
            #출력할때는 다시 -를 붙여서 +값을 뽑아온다
            print(-hq.heappop(a))
    #0이 아니면 push해야함
    #넣을때 부호를 바꿈.그럼 원래 큰값이 작아져서 위로 올라가게 됨
    else:
        hq.heappush(a,-n)