import sys
sys.stdin=open('input.txt','r')


#이 코드의 문제는, 3개만 뽑아서 최대를 구해야하는데 그게 안됨. 어떻게 고칠수있을까>


def DFS(L,SUM,cnt):
    global answer
    if SUM>M:
        return

    if L==N:
        if cnt==3:
            if SUM>answer:
                answer=SUM

    else:
        DFS(L+1,SUM+cards[L],cnt+1)
        DFS(L+1,SUM,cnt)


if __name__=="__main__":
    N, M = map(int, sys.stdin.readline().split())
    cards = list(map(int, sys.stdin.readline().split()))
    answer=0
    DFS(0,0,0)
    print(answer)



#for문으로 해보자


# N, M = map(int, input().split())
# cards = list(map(int, input().split()))
# answer = 0
#
# for i in range(0,N-2):
#     for j in range(i+1,N-1):
#         for k in range(j+1,N):
#             if cards[i]+cards[j]+cards[k] <= M and M-(cards[i]+cards[j]+cards[k]) < M-answer:
#                 answer=cards[i]+cards[j]+cards[k]
#
# print(answer)
