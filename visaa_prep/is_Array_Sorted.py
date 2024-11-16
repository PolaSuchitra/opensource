x=int(input())
arr=list(map(int,input().split()))
s=1
for i in range(1,x):
    if(arr[i-1]>arr[i]):
        s=0
        break
if(s==1):
    print("true")
else:
    print("false")
        
