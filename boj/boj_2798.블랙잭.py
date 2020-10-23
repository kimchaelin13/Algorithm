import sys
sys.stdin=open('input.txt','r')

'''
이 코드의 문제는, 3개만 뽑아서 최대를 구해야하는데 그게 안됨. 어떻게 고칠수있을까>


def DFS(L,sum):
    global answer
    if sum>M:
        return

    if L==N:
        if sum>answer:
            answer=sum

    else:
        DFS(L+1,sum+cards[L])
        DFS(L+1,sum)


if __name__=="__main__":
    N, M = map(int, input().split())
    cards = list(map(int, input().split()))
    answer=0
    DFS(0,0)
    print(answer)
'''

#for문으로 해보자


N, M = map(int, input().split())
cards = list(map(int, input().split()))
answer = 0

for i in range(0,N-2):
    for j in range(i+1,N-1):
        for k in range(j+1,N):
            if cards[i]+cards[j]+cards[k] <= M and M-(cards[i]+cards[j]+cards[k]) < M-answer:
                answer=cards[i]+cards[j]+cards[k]

print(answer)
