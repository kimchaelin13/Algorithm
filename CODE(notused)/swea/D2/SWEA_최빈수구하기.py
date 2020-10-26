import sys
sys.stdin = open("input1.txt", "r")

#리스트로 socres를 받는다. 그리고 전부다 sorted하고, 하나씩 읽어주면서
#그 중에 [0]*100 배열을 만든다
#그리고 만약에 그 리스트의 인덱스값과 socres안에 있는 j값이 같으면
#그 li[i]=j이렇게 추가해주고, 그 가장 많은 value를 가진 index를 뽑음
for tc in range(1,int(input())+1):
    case=int(input())
    scores= list(map(int,input().split()))
    numbers=[0]*100

    for i in range(len(numbers)):
        for j in scores:
            if i==j:
                numbers[i]+=1
    max=0
    for i in numbers:
        if i>max:
            max=i
            result=numbers.index(max)

    print('#{} {}'.format(tc,result))






