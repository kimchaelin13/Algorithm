import sys
sys.stdin = open("input.txt", "r")
result=[0]*10
nums=[]
for _ in range(3):
    nums.append(int(input()))

multi=1
for i in nums:
    multi=multi*i
#print(multi)

#17037300이 들어오면
#이걸 리스트에 집어넣을건데
#result의 인덱스값과 1이 같으면? 거기 +해줌

for j in str(multi):
    result[int(j)] += 1

for i in result:
    print(i)
