# import sys
# sys.stdin=open('input.txt','r')
#
# def DFS(L,sum): #sum에 내가 만든 부분집합의 원소를 다 누적할거임, L은 Level
#     if sum>total//2:
#         return
#     if L==n:
#         if sum==(total-sum):
#             print('YES')
#             sys.exit() #함수 종료가 아닌 프로그램 전체 종료
#     else:
#         DFS(L+1,sum+a[L]) #L은 인덱스번호라고 생각하자
#         DFS(L+1,sum)
#
# if __name__=="__main__":
#     n=int(input())
#     a=list(map(int,input().split()))
#     total=sum(a)
#     DFS(0,0)
#     print("NO")#만약에 아무경우가 없어서 재귀가 끝나버린 케이스라면, 돌아와서 NO가 찍힘
#


def DFS(v):
    if v == n + 1:
        for i in range(1, n + 1):
            if check[i] == 1:
                print(i, end=" ")
        print()  # 줄바꿈


    # 여기서 뻗어나가는거다. 사용한다.사용하지 않는다
    else:
        check[v] = 1
        DFS(v + 1)
        check[v] = 0
        DFS(v + 1)


if __name__ == "__main__":
    n = int(input())
    check = [0] * (n + 1)  # 어떨때 사용하는지,안했는지 체크변수
    DFS(1)