import sys
sys.stdin = open("input.txt", "r")

def DFS(L,sum):
    global res
    if L==n+1:
        #종료지점은 n+1, 이때 하나가 완성된것임
        if sum>res:
            res=sum
    else:
        # 현재L번째상담을 한다고 했을때,T[L]은 상담이걸리는 날짜
        # 그 날짜가 n+1보다 많으면 안되는것, 넘어가는거니까
        if L+T[L]<= n+1:#현재L번째상담을 한다고 했을때,T[L]은 상담이걸리는 날짜
            DFS(L+T[L],sum+P[L]) #L번째 상담을 하고 난 그 다음날
        #1씩 증가하다보면 당연히 n+1까지 가겠지
        DFS(L+1,sum) #상담을 하지 않는 경우

if __name__ == "__main__":
    n=int(input())
    T=[] #걸리는 시간
    P=[] #얻을 수 있는 금액

    for i in range(n):
        a,b=map(int,input().split())
        T.append(a)
        P.append(b)
    res=-987654321
    T.insert(0,0) #T를 날짜가 담겨있는 리스트로 볼건데, 1번인덱스-2(1일일때 4금액) 이렇게 볼려고!하나씩 미룸
    P.insert(0,0)
    DFS(1,0) #날짜가 넘어가고, 두번째인자는 얻을수있는금액
    print(res)