N,X,Y=map(int,input().split())
if(N*X<Y):
    print("NO")
elif((N*X>=Y) and (Y%X==0)):
    print("YES")
else:
    print("NO")
