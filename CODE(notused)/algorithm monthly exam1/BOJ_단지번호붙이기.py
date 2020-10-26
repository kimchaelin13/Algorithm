import sys
sys.stdin = open("input.txt", "r")
#우좌하상
di=[0,0,1,-1]
dj=[1,-1,0,0]

#이 체크함수는 뭉텅이안으로 들어온거임. 뭉텅이안에 있는 1을 세준다
def check(i,j):
    global home_cnt
    visited[i][j] = True
    home_cnt+=1

    for d in range(4):
        ni=i+di[d]
        nj=j+dj[d]

        if ni<0 or ni>=N or nj<0 or nj>=N:
            continue
        if visited[ni][nj]==True:
            continue
        if home_list[ni][nj]==False:
            continue
        check(ni,nj)


N=int(input())
home_list=[list(map(int,list(input()))) for _ in range(N)]
visited=[[0]*N for _ in range(N)]
home=[]
#home_list를 읽어주면서 만약에 원소가 1이고, visited에는 0이 찍혀있으면? 그때 home_cnt를 초기화함.그때 새로운 뭉텅이를 찾았다는 뜻임
#그리고 check함수를 불러올건데 이 함수는 뭉텅이안에 1을 다 세준다.
#그리고 그 체크함수를 통해서 나온 다 센 뭉텅이 하나를 리스트에 어펜드해준다

for i in range(N):
    for j in range(N):
        if home_list[i][j]==1 and visited[i][j]==False:
            home_cnt=0
            check(i,j)
            home.append(home_cnt)
print(len(home))
for h in sorted(home):
    print(h)

