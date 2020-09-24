import sys
sys.stdin=open('input.txt','r')


def check(nums):
    global ans
    #중간정산 cnt라고 생각하면 된다
    cnt = 1
    for i in range(1, N):
        #첫번째 if문, 만약에 첫번째수보다 두번째수가 크거나 같다면 ? cnt+=1
        if nums[i-1] <= nums[i]:
            cnt+=1
        #작다면, cnt=1로 초기화한다.
        else:
            cnt = 1

        #if문과 else문을 통과하고 나면 이 if문으로 무조건 들어오게 되고
        # 여기서 정산을 한다. 만약에 위에서 구한 cnt가 현재까지의 ans보다 크다면 계속 갱신해준다.
        if ans < cnt :
            ans = cnt


N = int(input())
arr = list(map(int, input().split()))

#최종 결과, 최솟값은 0이 아니라 1임
ans = 1

#오름차순체크
check(arr)
#리스트를 거꾸로 읽어주면서,식은 똑같이 쓰고 마치 내림차순인것처럼 오름차순과 같은 함수에 적용할 수 있다.
check(arr[::-1])
print(ans)

