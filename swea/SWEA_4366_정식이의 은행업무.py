import sys
sys.stdin=open('input.txt','r')

'''
1010 (2) => 한글자씩 바꿔서 10진수로 저장해서 결과를 어떤 리스트에 담는다

212(3) => 얘도 바꿔서 그 값이 위에 저장해놓은 리스트에 있으면, 그 값을 출력하고, break!
'''
for tc in range(1, int(input())+ 1):
    B = input()
    T = input()
    listB = []
    for i in range(len(B)):
        Temp = list(B)
        #1010의 하나씩 바꿔서 temp[i]를 바꿔주고
        Temp[i] = str((int(B[i]) + 1) % 2)
        #2진수로 바꿔서 append
        listB.append(int(''.join(Temp), 2))

    # result = -1
    for i in range(len(T)):
        Temp = list(T)
        for j in range(1,len(T)):
            Temp[i] = str((int(T[i]) + j) % 3)
            if int(''.join(Temp), 3) in listB:
                result = int(''.join(Temp), 3)
                break
        # if result > -1:
        #     break
    print('#{} {}'.format(tc, result))


# for tc in range(1,int(input())+1):
#     binary=input()
#     ternary=input()
#     binaryList=[]
