def fact1(n):
    if(n==0 or n==1):
        return 1
    else:
        return n*fact1(n-1)
n = int(input())
print(fact1(n))
