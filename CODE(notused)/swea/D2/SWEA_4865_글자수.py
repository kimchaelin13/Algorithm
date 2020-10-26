import sys
sys.stdin = open("input.txt", "r")

for test_case in range(1, int(input())+ 1):
    str1=input()
    str2=input()
    cnt, sub_cnt=0,0
    #str1, str2를 동시에 읽으면서
    #str1의 원소가 str2에 있다면,
    #몇개가 있는지 세고/그거 어디다가 넣어주고
    #반복하다가, cnt가 더 크면 그걸로 갱신함

    for i in str1:
        #sub_cnt는 중간정산을 하는 변수이다. 따라서 두번째로 x를 다세서 sub_cnt를 넣고
        #그 다음 문자를 또 세줄때는 다시 sub_cnt를 초기화하고, +1을 해줘야한다!
        sub_cnt = 0
        for j in str2:
            if i==j:
                sub_cnt+=1 #x가 몇개인지 세줌,
        if sub_cnt>cnt:
            cnt = sub_cnt

    print(f'#{test_case} {cnt}')

#쌤풀이
#카운트 배열, 체크배열 만들자, 내장함수 안쓸거임

T=int(input())
for tc in range(1,tc+1):
    str1=input()
    str2=input()

    check_arr=[0]*26
    count=[0]*26

    #1.str1을 순회하면서 알파벳 체크
    #첫번째 주어진 문장을 돌면서 사용된 글자를 전부 체크하는거임
    for i in str1:
         check_arr[ord(i)-ord('A')] =1


    #2. 체크된 알파벳의 카운트 세기
    for i in str2:
        if check_arr[ord[i]-65]==1:
            count_arr[ord[i]-65]+=1

    print('#{} {}'.format(tc,max(count_arr)))




