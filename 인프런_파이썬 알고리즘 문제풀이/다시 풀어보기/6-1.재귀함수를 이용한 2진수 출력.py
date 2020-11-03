import sys
sys.stdin=open('input.txt','r')
'''
10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하세요. 단 재귀함수를 이용
해서 출력해야 합니다.

11 => 2진수로 변환하기

#1. 만약 n==0이 되면 종료해서 res롤 반환한다
#2. 그게 아니라면, n%2을 문자열 res에 더하고
                n을 n//2로 갱신한다
'''

def change_to_bin(N):
    global res
    if N==0:
        res=res[::-1]
        return res
    else:
        res += str(N%2)
        N=N//2
        change_to_bin(N)

if __name__ == '__main__':
    for i in range(3):
        N=int(input())
        res=''
        change_to_bin(N)
        print(res)