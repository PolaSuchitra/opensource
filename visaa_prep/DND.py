N,m = map(int,input().split())
arr = list(map(int,input().split()))
sumd, sumn = 0, 0
for i in range(N):
    if(arr[i]%m==0):
        sumd+=arr[i]
    else:
        sumn+=arr[i]
print(sumd - sumn)
