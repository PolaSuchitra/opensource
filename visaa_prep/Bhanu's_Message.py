k=input()
if (k[0]=='+'and k[1:3].isdigit() and s[3]==" " and len(k)==14 and k[4:].isdigit() and sum(int(digit) for digit in k[4:])>0):
    print("Correct")  
else:
    print("Incorrect")
