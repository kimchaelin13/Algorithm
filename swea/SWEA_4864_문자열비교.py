import sys
sys.stdin = open("input.txt", "r")


'''
[문제 설명]
ABC

ZZZZZABCZZZZZ

두번째 문자열에 첫번째 문자열과 일치하는 부분이 있으므로 1을 출력.
 

ABC

ZZZZAZBCZZZZZ

문자열이 일치하지 않으므로 0을 출력.

[문제이해]
-패턴매칭이다!
-패턴매칭에서 배웠던 알고리즘? Burte Force!!
'''
#1 어제베운 brute force를 이용했다
# for test_case in range(1, int(input())+ 1):
#     str1=input()
#     str2=input()
#     A=len(str1)
#     B=len(str2)
#
#     for i in range(B-A+1):
#         cnt=0
#         for j in range(A):
#             if str2[i+j]==str1[j]:
#                 cnt+=1
#             else:
#                 break
#
#         if cnt==A:
#             result=1
#             break
#
#         else:
#             result=0
#
#     print(f'#{test_case} {result}')
#

#[다시 연습해보기]
import sys
sys.stdin = open("input1.txt", "r")

for tc in range(1,int(input())+1):
    pattern = input() #on
    sentence = input() #lemon
    A = len(pattern)
    B = len(sentence)
    cnt=0
    for i in range(B-A+1):
        for j in range(A):
            if sentence[i+j] == pattern[j]:
                cnt += 1
            else:
                break

        if cnt == A:
            result="1"
            break #패턴을 찾으면 1을 출력하고 빠져나오면 됨. break를 안넣으면 이미 패턴을 찾아도 다음 i로 넘어가게됨
        else:
            result="0"
    print("#{} {}".format(tc,result))

def check(str1,str2):
    for i in range(len(str2)-len(str1)+1):
        for j in range(len(str1)): #찾고 싶은 패턴이니까 얘를 계속 돌아야지
            #긴거는 한칸씩 옆으로 가면서 이동
            if str2[i+j] != str1[j]:
                break
        #중간에 걸리지 않았따면? else구문 실행
        else:
            return 1
    return 0



T=int(input())
for tc in range(1,T+1):
    str1=input()
    str2=input()
    print("#{} {}".format(tc,check(str1,str2)))