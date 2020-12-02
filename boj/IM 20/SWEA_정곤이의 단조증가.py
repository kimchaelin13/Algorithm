import sys
sys.stdin=open('input.txt','r')

'''
1
4
2 4 7 10

1 ≤ i < j ≤ N 인 두 i, j에 대해, Ai x Aj값 
-> 조합 곱 하나씩 만들어서 그 곱이 단조증가인지 아닌지 확인한다. 단조증가이고, 만약 이전의 MAX보다 크다면? 갱신
모든 조합의 곱을 다 돌리고, 맥스 출력

만약 Ai x Aj중에서 단조 증가하는 수가 없다면 -1을 출력한다.


'''

def isIncrease(multi):
    global MAX, flag
    str_multi = str(multi)

    if len(str_multi)==1:
        flag=0
        return

    for i in range(len(str_multi)-1):
        if int(str_multi[i]) > int(str_multi[i+1]):
            break
    #단조증가숫자라면, max와 비교해서 갱신
    else:
        flag=1
        if MAX<multi:
            MAX = multi

for tc in range(1,int(input())+1):
    N=int(input())
    nums=list(map(int,input().split()))
    MAX=0
    multi=0
    flag=0
    for i in range(0,N-1):
        for j in range(i+1,N):
            multi = nums[i] * nums[j]
            isIncrease(multi)

    if flag==1:
        print('#{} {}'.format(tc,MAX))
    else:
        print('#{} {}'.format(tc,-1))