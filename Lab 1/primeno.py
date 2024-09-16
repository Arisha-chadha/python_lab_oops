x=int(input("enter no"))
flag=0
for i in range (2,x,1):
    if (x%i==0):
         flag=1
if (flag==1):
    print("number is not prime")
else :
    print("number is prime")
