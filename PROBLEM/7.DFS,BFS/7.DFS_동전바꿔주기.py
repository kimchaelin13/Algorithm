import sys
sys.stdin = open("input.txt", "r")

def DFS(L,sum):
    global cnt

    if sum>T:
        return
    if L==k: #말단노드까지 왔을때
        if sum==T:
            cnt+=1
            return cnt


    else:
        #예를 들어, 5원짜리가 3개있으면
        #0,1,2,3 가지를 뻗는거임
        for i in range(cn[L]+1):
            #i가 1이면 1개 1개 사용할거야
            DFS(L+1,sum+(cv[L]*i))


if __name__=="__main__":
    T=int(input())
    k=int(input())
    cv=[] #coin value
    cn=[] #coin number
    for i in range(k):
        a,b=map(int,input().split())
        cv.append(a)
        cn.append(b)
    cnt=0
    DFS(0,0)
    print(cnt)


