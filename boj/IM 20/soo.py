'''
NxN 중제기설치'모두에게 원활한 통신 서비스 제공하기 위해 마을에 있는 모든 집들이 중제기의 통신 범위 안에 포함되도록 설치
통신범위 최소화 목표
입력으로 주어진 위치에 설치(x,y)
중제기의 통신범위는 원모양 반지름 R의 범위는 1~N이하정수
마을에 있는 집 위치와 중제기의 위치가 입력으로 주어짐
마을의 모든 집 들어오는 중제기 통신범위 R의 최소값 구하기
집과 중제기의 좌표가 각각 (x1,y1),(x2,y2)
D**2 = (x1-x2)**2+(y1-y2)**2
집과 중제기간 거리 D의 제곱이 반지름 R의 제곱보다 작거나 같을 경우 포함!!

각집과 중계기간 거리를 모두 구한뒤, 그 최댓값까지 포함하는 반지름 구하기
'''
import sys
sys.stdin = open('input.txt','r')

def dist(i,j):
    global distmax
    ji,jj = J
    hi,hj = i,j
    D = ((hi-ji)**2 +(hj-jj)**2)**(0.5)
    if D > distmax:
        distmax = D
    return


T = int(input())
for tc in range(1,T+1):
    N = int(input())
    # 0:빈공간, 1:집,2:중계기
    arr = [list(map(int,input().split())) for _ in range(N+1)]
    MIN = 987654321
    home = []
    for i in range(N+1):
        for j in range(N+1):
            if arr[i][j] == 2:
                J = [i,j]
            if arr[i][j] == 1:
                home.append([i,j])
    # 집과 중계기간 거리 중 최댓값 구하기
    distmax = 0
    for di,dj in home:
        dist(di,dj)
    # print(distmax)
    for r in range(N+1):
        if r>=distmax:
            print('#{} {}'.format(tc,r))
            break

