#한 줄을 읽어서 정수로 변환

#input() : 한줄을 읽어옴
#int(): int형으로 변환
N = int(input())
print(N,type(N))

#한 줄을 읽어서 공백으로 구분된 문자를 입력받기
#input().split() : 한 줄 읽고, 구분문자로 나눠서 문자로 이루어진 리스트로 반환!
#print(input().split()) #['a','b','c']

#한 줄을 읽고, 공백으로 구분된 문자 -> 개수가 정해져 있음.
# 1 2 만 들어온다고 하면 ?
#N,M = input().split()
#print(N,M)
#print(type(N),type(M)
# 꿀팁: 영역 선택하고, 컨트롤 + d 복사 / 그리고 영역선택하고 shift+ALT+방향키 움직임
#문자열로 받은 N,M을 int로 바꾸고 싶다면?
#map 함수를 이용해서 map(int, input().split())으로!!

#1차원 배열입력받기!!
# 1 2 3 4 5를 입력받는다고 해보자
arr = input().split()
#그런데 이걸 그대로 출력한다고 하면 ['1','2','3',,] 이런식으로 됨!
#int형태로 변환해주자!
arr = list(map(int,input().split()))
#list(): 괄호안의 데이터를 리스트로 묶어서 리턴!!











