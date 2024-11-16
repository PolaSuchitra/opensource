x=int(input())
sum1=0
while(x!=0): 
    sum1 = sum1 + (x%10)
    x=x//10
if((sum1%2) == 0):
    print("Vignesh")
else:
    print("Charan")
