import sys
sys.stdin=open('input.txt','r')

board=[list(map(int,input().split())) for _ in range(5)]
temp=[list(map(int,input().split())) for _ in range(5)]
nums=[]
for i in range(5):
    for j in range(5):
        nums.append(temp[i][j])

cnt=0
res=0
for n in range(len(nums)):
    for i in range(5):
        for j in range(5):
                if nums[n] in board[i][j]:
                    board[i][j]=0

                    if board[i][:]==0:
                        cnt+=1
                    elif board[j][:]==0:
                        cnt+=1

                if cnt==3:
                    res=nums[n]
                    break
print(res)

