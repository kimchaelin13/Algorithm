import sys
sys.stdin=open('input.txt','r')

'''
지원자의 입장, 내가 어떤 사람보다 키가 작으면? 몸무게는 높아야 뽑히는것

5
172 67
183 65
180 70
170 72
181 60

#1.키순으로 내림차순 정렬
#2.첫번째 사람은 키로 다 이김(키 1등), 몸무게 다 져도 상관 없음, 이사람무조건 cnt+=1
    두번째 사람입장에서는 자기보다 키가 큰 사람(1번째 사람)만 생각하면 된다.
    왜냐면 얘는 뒤에 나올 애들중에 키 1등이니까.(몸무게 볼 필요없음)
#3. 세번째 사람입장에서도 나보다 키큰 사람만 체크하면 된다. 나를 키로 이기는 위사람들만
    살펴서 나보다 몸무게 다 적으면 cnt+1
    
    ...
#4. 정렬을 하면=> 키는 볼필요가 없고,몸무게만 
    largest=0해서 몸무게 최대값 갱신 => 갱신되면 cnt+=1    
'''


N=int(input())
body=[]
for i in range(N):
    a,b=map(int,input().split())
    body.append((a,b))

#키순으로 내림차순정렬, 이렇게 하면 첫번째 자료기준으로 내림차순
body.sort(reverse=True)

#몸무게 최대값이 달라지면? 그건 걔를 선택한다는 거니까 cnt+1
largest=0
cnt=0
for h,w in body:
    if w>largest:
        largest=w
        cnt+=1
print(cnt)