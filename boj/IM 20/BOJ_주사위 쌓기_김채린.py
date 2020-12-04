import sys
sys.stdin=open('input.txt','r')

'''
5
2 3 1 6 5 4
3 1 2 4 6 5
5 6 4 1 3 2
1 3 6 2 4 5
4 1 6 5 2 3

1 아래위에 6이 없는 경우 최댓값 6
2 아래위에 6은 있고, 5는 없는 경우, 최댓값 5
3 아래위에 5,6 모두 있는경우, 최댓값 4
매치인덱스 - [5,3,4,1,2,0]


일단 아래주사위가 정해지면, 위는 다 정해짐
아래 주사위만 정하면 됨, -> 아래 주사위의 윗면을 1~6까지로 설정했을때 최댓값을 구한다

생각
1번 주사위의 윗면이 1일때 => 옆면의 최대는 6이다
이건 어떻게 나왔냐면, 1번이 있는 인덱스는 2(주사위 배열)이다. 그리고 매치[2]와 연결된 값은 4이다.
따라서 1의 아랫면은 주사위[4]이다. 그리고 주사위[2], 주사위[4] 모두 5,6이이 아니므로 옆면의 최댓값은 6이 된다

다음으로 2번
2번의 아랫면은 1번에 의해서 정해짐. => 2번의 아랫면은 1이다.
2번의 윗면은, 4이다.(주사위2에서 1이 있는 인덱스는 1이고, 매치[1]은 3 => 주사위2[3]=4 
둘다 5,6이 아니므로 최댓값은 

이런식으로 1번을 1~6까지 다하고 최댓값을 갱신해서 마지막에 프린트한다.
'''


def choose(dicelist, idx):
    oidx = opposite[idx]
    MAX=0
    for i in range(6):
        if i==idx or i==oidx:
             continue
        if MAX<dicelist[i]:
            MAX = dicelist[i]
    return MAX

N=int(input())
dices = [list(map(int,input().split())) for _ in range(N)]
opposite = [5,3,4,1,2,0]
ans=0

for i in range(6):
    tmp = choose(dices[0],i)
    next = dices[0][opposite[i]]

    for j in range(1,N):
        idx = dices[j].index(next)
        tmp += choose(dices[j],idx)
        next = dices[j][opposite[idx]]

    if tmp>ans:
        ans=tmp
print(ans)