x=int(input())
i=1
for j in range(1,x+1):
    for k in range(j):
        print(i,end=" ")
    i=i+1
    print(" ")
