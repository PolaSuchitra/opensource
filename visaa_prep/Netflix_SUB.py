a,b,c,z=map(int,input().split())
if((a+b>=z) or (b+c>=z) or (c+a>=z)):
    print("YES")
else:
    print("NO")
