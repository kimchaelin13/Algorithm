import sys
sys.stdin=open('input.txt','r')

'''
flatten

5
5 7 7
1
5 10 6 3 8
100
10 10 10 10

리스트 배열로 받고,

while [0]이 리스트의 맥스가 되면 스탑

아니라면, 1부터 끝까지의 값중에 가장 큰 값을 찾고, 거기서 -1,하고 타겟에 +1해줌 이걸 반복함
'''
votes = list(map(int,input().split()))
if len(votes) == 1: print(0)
else:
    myvote = votes.pop(0)
    cnt = 0
    while myvote <= max(votes):
        votes[votes.index(max(votes))] -= 1
        myvote += 1
        cnt += 1
    print(cnt)

# def max_serach():
#     global max_idx
#     max_val=-1
#
#     for i in range(1,len(vote)):
#         if vote[i] > max_val :
#             max_val = vote[i]
#             max_idx = i
#     return max_idx
#
# for tc in range(1,int(input())+1):
#     vote=list(map(int,input().split()))
#     cnt=0
#     flag=0
#     if len(vote)==1:
#         flag=1
#     if flag==0:
#         target=vote[0]
#         max_idx = 0
#
#         while True:
#             vote[max_serach()] -=1
#             target +=1
#             cnt+=1
#             if target>vote[max_serach()]:
#                 break
#     print('#{} {}'.format(tc,cnt))

