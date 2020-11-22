import sys
sys.stdin=open('input.txt','r')

'''
뒤에서부터 3개씩 끊어서,계산함 
1100100

=> 100이면, 3번을 돌면서, 1이면 2**2 +더해주고 2**2//2 로 갱신하고, 다음은 0이니까 넘어가고
또 그걸 //2로 갱신해줌 0이면 0을 더하고, 1이면 그에 해당하는 숫자를 더한다
'''

N=list(map(int,input()))

for i in range(len(N)):
