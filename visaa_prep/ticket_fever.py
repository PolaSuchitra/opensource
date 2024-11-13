x = int(input())
for i in range(x):
    y,z= map(int,input().split())
    k = y - z
    if(k<0 or k==0):
        print(0)
    else:
        print(k)
