def perm(n,k): #원하는 depth n이고, 현재k
    if k==n:
        print(arr)

    else:
        #k부터 n-1까지
        for i in range(k,n):
            arr[k],arr[i]=arr[i],arr[k]
            perm(n,k+1)
            arr[k],arr[i]=arr[i],arr[k]



arr=[1,2,3]
N=len(arr)
perm(N,0)