str1='onemonon'
str2='on'

def BruteForce(str1,str2):
    A = len(str1)
    B = len(str2)

    for i in range(A-B+1): #A안에 B찾기(index설정)
        cnt = 0
        for j in range(B): #문자가 같은지 비교
            if str1[i+j] == str2[j]:
                cnt += 1
            else:
                break
        if cnt == B: #str2의 len과 일치하기 때문에 같은패턴 찾음
            return i
    return -1 #발견하지 못한다면 검색실패로 -1반환
tmp = BruteForce(str1,str2)
print(tmp)