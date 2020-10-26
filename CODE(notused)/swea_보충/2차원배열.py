#2차원 배열은 1차원 리스트를 묶어놓은 리스트이다


#2차원 배열 선언
# arr =[[0,1,2,3],[4,5,6,7]]
# print(arr)


#0으로 가득찬 배열
arr_1=[[0]*5 for _ in range(5)]
print(arr_1)
#arr=[]

#2차원 배열받기
'''
3 4
0 1 0 0
0 0 0 0
0 0 1 0
'''
#1차원 리스트 들어갈 배열이 들어가야하고,얼만큼/n만큼
#이걸 이어붙이기식으로 할거야


N,M=map(int,input().split())
mylist=[0 for i in range(N)] #1차원 배열 초기화

list(map(int,input().split())) #1차원 배열 입력받아서 리스트로 받기, 이 리스트는 1차원

#초기화를 해놔서 접근 가능한것임
for i in range(M):
    mylist[i] = list(map(int,input().split()))