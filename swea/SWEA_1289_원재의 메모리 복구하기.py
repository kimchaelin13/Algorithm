import sys
sys.stdin=open('input.txt','r')

'''
1110001

-> 연속된 1 뭉텅이 / 연속된 0 뭉텅이 각각 구해주기

규칙: 바꾸고자 하는 값의 맨앞이 0이면 두개 더해서 -1 
    1이면 그냥 더함
'''

for tc in range(1,int(input())+1):
    S=list(map(int,list(input())))
    N=len(S)
    res=[]
    for i in range(0,N-1):
        if S[i] != S[i+1]:
            res.append(S[i])
    res.append(S[-1])

    zero=res.count(0)
    one=res.count(1)
    #print(tc)
    #print(zero,one)

    if S[0] == 0:
        print('#{} {}'.format(tc,zero+one-1))
    else:
        print('#{} {}'.format(tc,zero+one))