'''
합이 100이 되는 애들만 출력 = 토탈-어떤애-어떤애 = > 100이 되면, 걔네 뺴고 출력하기
'''


import sys
sys.stdin=open('input.txt','r')

h=[]
for _ in range(9):
    h.append(int(input()))
h.sort()
total= sum(h)
N=9
flag=0
for i in range(N-1):
    for j in range(i+1,N):
        if total - h[i] - h[j] == 100:
            for k in range(N):
                if k!=i and k!=j:
                    print(h[k])
            flag=1
            break
    if flag:
        break
