x,y=map(int,input().split())
if(y%100==0):
    z = y/100 
else:
    z = y/100 + 1
if(z>x):
    print(int(z-x))
else:
    print(0)
