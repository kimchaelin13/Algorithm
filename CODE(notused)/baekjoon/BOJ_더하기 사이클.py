import sys
sys.stdin = open("input.txt", "r")

'''
26을 받으면? 이걸 잘라서 써야겠당

#문자열로받아서
temp=26

#여기는 문자열
fir=temp[0]
sec=temp[1]

#더해줄땐 int로 다시바꿈
new_temp=int(fir)+int(sec)

#새로운 숫자를 만둘자
#new=str(sec)+str(new_temp)

#while로 돌려야겠다
#new까지하고 카운트 +1
#그리고 만약에 다시 원래 temp와 같아지면 그때 print(cnt) break
'''

# origin=input()
# made=''
# made=origin
# cnt=0
# new=''
# while True:
#     if new==origin:
#         print(cnt)
#         break
#     fir,sec=made[0],made[1]
#     temp=int(fir)+int(sec)
#     new=str(sec)+str(str(temp)[1])
#     made=new
#     cnt+=1


'while문 안에서 다 처리하고 싶은데 어떻게 해야하지????'

origin=int(input())
temp=origin
cycle=0

while True:
    new=(temp//10)+(temp%10)
    new_num=(temp%10)*10+(new%10) #이게 68이 나옴
    cycle+=1
    temp=new_num
    if origin == new_num:
        print(cycle)
        break





