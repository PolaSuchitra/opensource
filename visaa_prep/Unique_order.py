x=int(input())
arr=list(map(int,input().split()))
r=[]
for i in arr:
    if(i not in r):
        r.append(i)
for i in r:
    print(i,end=" ")
