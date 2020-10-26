import sys
sys.stdin = open("input2.txt", "r")
'''
부분집합의 합을 구하는 것과 동일한 패턴
만약에 레벨 끝까지 갔을때, 합한것이 B보다 크거나 같은걸 result에 모두 담아준다
그리고 출력할때, result의 min값에서 B를 빼줌
'''
def DFS(L,sum):
    if L==N:
        if sum >= B:
            result.append(sum)
    else:
        DFS(L+1,sum+heights[L])
        DFS(L+1,sum)


for tc in range(1,int(input())+1):
    N,B=map(int,input().split())
    heights=list(map(int,input().split()))
    result=[]
    DFS(0,0)
    print('#{} {}'.format(tc,min(result)-B))

