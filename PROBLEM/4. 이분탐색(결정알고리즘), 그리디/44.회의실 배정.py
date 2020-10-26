import sys
sys.stdin=open('input.txt','r')

'''
5 회의개수
1 4
2 3
3 5
4 6
5 7

#1. 입력받고
#2. (n+1)만큼 for문을 돌면서 첫번쨰 회의를 선택했을때,
    if 첫번째의 끝나는 시간보다 크거나 같은 그 다음 시작시간의 회의가 있다면 cnt+1
    
    그리고 그걸 res에 담아놓고, cnt>res: res=cnt
    
    근데 그래프로 풀고 싶었는데, 회의가 언제끝날지 모름 => 그래프 [][] 하는게 어려울듯
    
______________________________________

#1.회의 수 입력받고
#2.(N)만큼 돌면서 []에 (2,3)을 다 튜플 형태로 append해준다
#3.최대회의를 할려면, 시작시간이 앞선게 아니라 끝나는 시간이 앞서는 회의를 선택해나가야함
    #2에서 받은 리스트를 끝나는 시간을 기준으로 오름차순 정렬한다.
#4.그리고 그때는 첫번째 무조건 선택하는거니까, 리스트의 길이만큼 for문을 돌면서, 
    그 첫번째의 끝나는 시간을 그 다음의 시작시간으로 갱신할수있다면 cnt+=1
        
'''

N=int(input())
timeline=[]
for _ in range(N):
    a,b=map(int,input().split())
    timeline.append((a,b))
#print(timeline)

timeline.sort(key=lambda x:(x[1],x[0]))
print(timeline)

et=0
cnt=0
for s,e in timeline:
    if s>=et:
        print(et)
        et=e
        cnt+=1

