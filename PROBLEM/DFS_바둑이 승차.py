import sys
sys.stdin = open("input.txt", "r")

#부분집합을 다 구해줄거임
#부분집합의 sum을 구해서 result리스트에 넣고, 그 max값을 출력
#근데 그 부분집합의 sum은 259,즉 c를 넘지 않게 한다.


def DFS(L,sum):
    global result
    if sum>C:
        return
    if L==N:
        if sum>result:
            result=sum

    else:
        DFS(L+1,sum+weights[L])
        DFS(L+1,sum)


if __name__=="__main__":
    C,N=map(int,input().split())
    weights=[]
    for _ in range(N):
        weights.append(int(input()))
    #print(weights)
    result=-123456
    DFS(0,0)
    print(result)