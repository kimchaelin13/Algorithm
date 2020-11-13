'''
오름차순으로 정렬하고 자르고, 최대값 찾고
            세로도 마찬가지로 최댓값 찾아서
            두개 곱함
'''
import sys
sys.stdin=open('input.txt','r')

def hor_max(e):
    #마지막 e를 리턴해줌(마지막 e가 제일 크니까
    global HOR,HOR_s,HOR_e
    temp=e-HOR_s
    if temp>HOR:
        HOR=temp
    HOR_s=e
    if e>HOR_e:
        HOR_e=e

def ver_max(e):
    global VER,VER_s,VER_e
    temp=e-VER_s
    if temp>VER:
        VER=temp
    VER_s=e
    if e>VER_e:
        VER_e=e

N,M=map(int,input().split())
temp=[]
for _ in range(int(input())):
    D,C=map(int,input().split())
    temp.append((D,C))
temp.sort()

HOR,VER=0,0
HOR_e,VER_e=0,0
HOR_s,VER_s=0,0
for i in range(len(temp)):
    if temp[i][0]==0:
        hor_max(temp[i][1])
    else:
        ver_max(temp[i][1])

#3단계
#구한 HOR값과 M-e해서 둘중에 max값인걸로 출력해야함
RES=(max((M-HOR_e),HOR))*(max((N-VER_e),VER))
print(RES)


'''
import sys
input = sys.stdin.readline

N, M = map(int, input().split())

G1 = [0, N]
G2 = [0, M]

T = int(input())
for _ in range(T):
    d, num = map(int, input().split())
    if d == 0:
        G2.append(num)
    else:
        G1.append(num)
max_n = 0
G1.sort()
G2.sort()

for i in range(len(G1)-1):
    for j in range(len(G2)-1):
        area = (G1[i+1]-G1[i])*(G2[j+1]-G2[j])
        max_n = max(max_n, area)
print(max_n)


'''

'''
col,row = map(int,input().split())

colArr=[0, col] 
rowArr=[0, row]

n = int(input())
for i in range(0, n):
	t, p = map(int,input().split())
	if(t==0):
		rowArr.append(p)
	elif(t==1):
		colArr.append(p)

colArr.sort()
rowArr.sort()

maxCol = 0
maxRow = 0
for i in range(0, len(colArr)-1):
	maxCol=max(maxCol,colArr[i+1] - colArr[i])
for i in range(0, len(rowArr)-1):
	maxRow=max(maxRow,rowArr[i+1] - rowArr[i])

print(maxCol*maxRow)
'''