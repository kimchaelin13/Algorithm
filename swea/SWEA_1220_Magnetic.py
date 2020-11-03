import sys
sys.stdin = open("input2.txt", "r")
'''
빨은 1, 파는 2 이렇게 되어있음.
맨처음에 빨강을 먼저 만나야함. 파랑을 만나면 그냥 바로 n극으로 빨려들어가서 사라지니까!
그래서 맨청므에 빨간색을 먼저 만나야 하기 때문에 state를 빨로 설정
교착상태는 빨간색.파란색이 넘어가야 교착상태가 나오니까!! 
그리고 빨로 만나야하는데 마침 그자리가 빨간색이라면!! 그럼 우리는 이제 파란색을 만나야함. 그래야 교착상태가 발생하니까!
'''

for tc in range(1,11):
    N=int(input())
    arr=[(input().split()) for _ in range(100)]

    ans=0

    for i in range(N):
        #내가 만나야 될 컬러
        state=1
        for j in range(N):
            #내가 빨강을 만나야하고 마침 내자리가 빨강이라면
            if state==1 and arr[j][i] == '1':
                state=2
            #내가 파랑을 만나야 하고 마침 내자리가 파랑이라면, 교착상태 1증가
            elif state==2 and arr[j][i]=='2':
                state=1
                ans+=1
    print('#{} {}'.format(tc,ans))

