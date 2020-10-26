import sys
sys.stdin = open("input2.txt", "r")
'''
한번거쳤던 격자판을 다시 가도 됨. 0에서 시작할 수 도있음. 격자판 벗어나면 안됨
서로 다른 일곱자리의 수를 모두 담은 리스트의 len을 구한다
그 리스트안의 element들이 모두 겹치면 안된다. set자료구조이용


'''
di = (0, 0, -1, 1)
dj = (-1, 1, 0, 0)


def DFS(i,j,sen):
    global result

    if len(sen) ==7:
        result.add(sen)
        return

    for d in range(4):
        ni=i+di[d]
        nj=j+dj[d]

        if ni<0 or ni>=4 or nj<0 or nj>=4:
            continue
        DFS(ni,nj,sen+arr[ni][nj])

for tc in range(1,int(input())+1):
    arr=[input().split() for _ in range(4)]
    result=set()

    for i in range(4):
        for j in range(4):
            DFS(i,j,arr[i][j])
    print('#{} {}'.format(tc,len(result)))



