import sys
sys.stdin=open('input.txt','r')

# MSG_FORMAT = "{}번 원반을 {}에서 {}로 이동"
#
#
# def move(N, start, to):
#     print(MSG_FORMAT.format(N, start, to))
#
# def hanoi(N, start, to, via):
#     if N == 1:
#         move(1, start, to)
#     else:
#         hanoi(N-1, start, via, to)
#         move(N, start, to)
#         hanoi(N-1, via, to, start)
#
# hanoi(3, 'A', 'C', 'B')



#원반을 옮기는 순서

def hanoi(n,from_pos,to_pos,aux_pos):
    if n==1:
        print(from_pos,to_pos)
        return

    #원반 n-1개를 auxpos로 이동
    hanoi(n-1,from_pos,aux_pos,to_pos)
    print(from_pos,to_pos)
    hanoi(n-1,aux_pos,to_pos,from_pos)

n=int(input())
print((2**n)-1)
hanoi(n,1,3,2)



