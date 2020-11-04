import sys
sys.stdin=open('input.txt','r')
'''
두개를 같이 보면서
만약에 정답이면? tmp+=1 그때부터 누적하니까
그리고 만약에 오답이면? tmp=0
그리고 정답이든 오답이든 아래서 total+=tmp
'''
tc=int(input())

for tc in range(1,tc+1):
    N, M = map(int, input().split())
    answer = list(map(int, input().split()))
    total=0
    temp=0
    for i in range(M):
        student = list(map(int, input().split()))
        if answer[i]==student[i]:
            temp+=1
        else:
            temp=0
        total+=temp
    print('#{} {}'.format(tc,total))

