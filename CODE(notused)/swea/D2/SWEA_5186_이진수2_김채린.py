import sys
sys.stdin=open('input.txt','r')


def two(N):
    global result, cnt
    while True:
        NN = N * 2
        #print(next_num)
        result += str(int(NN))
        #print(result)
        N = NN - int(NN)
        cnt += 1
        if N == 0.0:
            return
        if cnt > 13:
            return

if __name__=='__main__':
    for tc in range(1, int(input())+1):
        N = float(input())
        result = ''
        cnt = 0
        two(N)
        flag=0
        if cnt > 13:
            print('#{} overflow'.format(tc))
        else:
            print('#{} {}'.format(tc,result))