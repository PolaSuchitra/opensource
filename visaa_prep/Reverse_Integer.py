x=int(input())
if x<0:
    k=-1
else:
    k=1
x=abs(x)
r = int(str(x)[::-1])
if r>2**31-1 or r<-2**31:
    print(0)
else:
    print(r*k)
