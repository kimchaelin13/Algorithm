import sys
sys.stdin=open('input.txt','r')

'''
3
3
0 18 34
48 0 55
18 7 0
4
0 83 65 97
82 0 78 6
19 19 0 82
6 34 94 0
5
0 9 26 85 42
14 0 84 31 27
58 88 0 16 46
83 61 94 0 17
40 71 24 38 0

N=3이면 [1,2,3,1][1,3,2,1]가능
=> (1,2)+(2,3)+(3,1)/(1,3)+(3,2)+(2,1)가능

그러면 만약에 N=3이면, (2~3)까지 가능한 조합을 구함. 조합 하나 구하면 => 2 3 리스트에 넣고, 
                                                                그거 앞 뒤에 1을 붙여줌

만약에 n=4이면 (2~4)까지의 조합을 구하는데 길이는 n-1
'''

from itertools import permutations
import math

for tc in range(1,int(input())+1):
    N=int(input())

    #조합 돌릴 리스트
    a=[]
    for i in range(2,N+1):
        a.append(i)

    arr=[list(map(int,input().split())) for _ in range(N)]
    #print(arr)

    #1.조합 리스트 만들기, N=3이면 [1,2,3,1]/[1,3,2,1] 만들기
    for i in range(math.factorial(N-1)): #3이니까, 2!=2, 총 두개의 경우리스트가 나오기 때문에
        temp=list(permutations(a,N-1))

    #2.[1,2,3,1]/[1,3,2,1] 만들기
    Temp=[]
    for j in temp:
        for k in range(len(j)):
            Temp.append(j[k])
    #2-1
    #print(Temp)
    res=[]
    fin=0
    bin=[]
    for i in range(0,len(Temp),N-1):
        res = Temp[i:i+(N-1)]
        #print(res)
        res.insert(0,1)
        res.append(1)
        print(res)

        #3.이제 ans(합)를 갱신해준다 ㅋㅋ
        ans=0
        total=987654321
        ansLst = []

        for i in range(len(res)-1):
            ans+=arr[res[i]-1][res[i+1]-1]
        bin.append(ans)
        
        #만약에 지금 구한 ans답이 전에 구한 ans(total)보다 더 작다면? total=ans
        if ans<total:
            total=ans
            print(tc,total)
    print('#{} {}'.format(tc,min(bin)))