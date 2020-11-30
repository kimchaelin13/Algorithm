import sys
sys.stdin=open('input.txt','r')

'''
#1.5
#2 0
#3.11118
#4.58
#5.84580
'''

for tc in range(1,int(input())+1):
    N=list(map(int,list(input())))
    targat_page = ''
    for i in N:
        targat_page += str(i)
    if targat_page == '100':
        print('#{} {}'.format(tc,0))
    targat_page=int(targat_page)
    targat_page=int(targat_page)
    broken=list(map(int,input().split()))
    # work = [i for i in range(0,10) if i not in broken]
    remote = [i for i in range(0,10)]
    for i in range(10):
        if i in broken:
            remote[i] = False
    print(remote)
    temp_1,temp_2='',''
    s=1
    for i in N:
        if remote[i] != False:
            temp_1 += str(remote[i])
            temp_2 = temp_1
        elif i in broken:
            print(remote[i])
            while True:
                if remote[i+s]!=False or remote[i-s]!=False:
                    break
                else:
                    s+=1
    temp_1 += str(remote[i+s])
    temp_2 += str(remote[i-s])
    res = min(abs(targat_page-int(temp_1)), abs(targat_page-int(temp_2)))
    print('#{} {}'.format(tc,len(N)+2))