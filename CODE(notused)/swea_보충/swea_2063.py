import sys
sys.stdin = open("input.txt", "r")

N = int(input())
arr=list(map(int,input().split()))

#버블정렬

#계속 바꾸는 작업, 큰 숫자를 뒤로 보내는게 목적임
for i in range(0,N-1):
    for j in range(i+1,N):
        if arr[i] > arr[j]:
            arr[i],arr[j] = arr[j],arr[i]
print(arr[N//2])


