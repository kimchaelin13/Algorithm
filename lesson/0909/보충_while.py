'''
while
반복문
- 기본 구조
    : 조건이 참인 동안 반복, 조건이 참이여야 돌아간다!
    : 조건식 => 결과가 참/거짓을 판별할 수 있음

반복문에서 사용
    -break: 반복문을 빠져나감
    -continue: 해당 반복만 안하고 다음 반복으로 넘어감
함수에서 함수를 종료하려면?
    return

횟수가 정해져 있다면? --> for
반복을 하다가 어떤 조건을 더 이상 만족 안하면 반복 종료 => while


'''

#자릿수 더하기
'''
6789
'''

N=int(input())
sum=0
#N을 갱신 -> N이 0이 되면 그만해 -> 0이 아닌동안 돌아
while N!=0:
    d=N%10
    sum+=d
    N=N//10
print(sum)