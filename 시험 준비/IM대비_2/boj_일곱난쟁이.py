import sys
sys.stdin=open('input.txt','r')
'''
접근: 난쟁이 9명 전체 키합 - 특정 2명 == 100일때, 그때의 특정 2명애들을 빼고 프린트하는거다.
그리고 처음부터 sort를 해야함 

'''
heights= []
for _ in range(9):
    heights.append(int(input()))
heights.sort()

for i in range(9): #특정 두명이 겹치지 않기 위해, 범위 설정을 이런식으로 함
    for j in range(i,9):
        if sum(heights)-heights[i]-heights[j]==100:
            #그때 찾은거임 i와 j를 그러면 이걸 프린트해야되니까
            #세번째 for문은 출력을 위한 for문이라고 생각하면 된다
            for k in range(9):
                if k!=i and k!=j:
                    print(heights[k])
            #프린트 한번 다하면 그때 함수를 아예 나와야함!!
            exit()
