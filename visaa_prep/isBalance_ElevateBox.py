N = int(input())
arr=list(map(int,input().split()))
b=[]
suml,sumr=0,sum(arr)-arr[0]
for i in range(N):
    if(i==0):
        b.append(abs(suml-sumr))
    else:
        suml+=arr[i-1]
        sumr-=arr[i]
        b.append(abs(suml-sumr))
print(' '.join(map(str,b)))
