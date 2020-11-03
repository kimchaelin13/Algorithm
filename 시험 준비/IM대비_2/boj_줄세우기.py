import sys
sys.stdin=open('input.txt','r')

'''
line[i]번째 자리에 i+1를 넣어라(insert함수이용)
ㅁ
0 1 1 3 2 면,
for문을 돌면서
i=0이면, 
0(line[0])번째 자리에 i+1를 넣어라.
그리고 그걸 뒤집어서 다시 어떤 리스트에 넣은 다음에 출력한다. 
'''
N=int(input())
line=list(map(int,input().split()))
result=[]

for i in range(N):
    result.insert(line[i],i+1)

final=result[::-1]
print(*final)