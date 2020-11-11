import sys
sys.stdin=open('input.txt','r')

'''
<problem>17413<is hardest>problem ever<end>
1eno 2owt 3eerht rruof4 evif5 xis6


if,'<'를 만나면 '>'를 만날때까지 계속 res에 담는다.
else, 
    문자를 어떤 리스트에 담을건데,띄워쓰기 또는 '<'를 만나면 멈춰야 함
    멈추고 난 뒤, 담은 리스트를 뒤로 읽으면서 res에 더해준다.
'''
words = list(input())
words_length = len(words)
cnt = 0
while cnt < words_length: #cnt가 문자열 전체의 길이보다 작을때까지 반복하는데
    if words[cnt] == '<':
        for i in range(cnt + 1, words_length):
            if words[i] == '>':
                break
        cnt = i + 1
    elif words[cnt] == ' ':
        for i in range(cnt + 1, words_length):
            if words[i] != ' ' or words[i] != '<':
                break
        cnt = i
    else:
        for i in range(cnt + 1, words_length):
            if words[i] == ' ' or words[i] == '<':
                end, r_end = (i - 1), i
                break
        else: end, r_end = (words_length - 1), words_length
        while cnt < end:
            words[cnt], words[end] = words[end], words[cnt]
            cnt += 1
            end -= 1
        cnt = r_end
print(''.join(words))