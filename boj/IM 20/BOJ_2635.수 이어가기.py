import sys
sys.stdin=open('input.txt','r')

'''
100이 주어지면,1부터 99까지 탐색하면서
1일때, while문을 이용해서 어디까지 갈수있는지체크함 -가 나오면 멈추게 하고, 리스트에 append

for i in range(100):
    check[i]
    
    if CNT>MAX:
        MAX=CNT
        MAX_LIST = LIST
'''


#v=false로 기본값으로 정함
def f(a, b, v=False):
    i = 1
    while b >= 0:
        if v: print(a, end=' ')
        a, b = b, a - b
        i += 1
    if v: print(a, end=' ')
    return i


n = int(input())
L = [f(n, i) for i in range(n + 1)] #0~n까지 어떤 숫자를 택했을때 가장 긴지 계산해놓고, 배열을 만들때는 해당인덱스로만 답을 구한다!
print(L)
k = L.index(max(L))
#print(max(L))
f(n, k, 1) # ? : f(n,k,1)을 호출하면 왜 i값은 안돌려주지??



'''
내 코드
def check(pre,nex):
    global tmp
    tmp_list.append(pre)
    tmp_list.append(nex)

    while True:
        if pre-nex<0:
            break
        tmp+=1
        tmp_list.append(pre-nex)
        pre=nex
        nex=tmp_list[-1]

N=int(input())
res=0
res_list=[]
for i in range(N+1):
    tmp=2
    tmp_list=[]
    check(N,i)

    if tmp>res:
        res=tmp
        res_list = tmp_list
print(res)
print(*res_list)
'''
