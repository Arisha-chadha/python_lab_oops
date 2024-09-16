x=int(input("enter number"))
temp=x;
sumn=0
length = len(str(x))
while temp!=0:
     
     a=(temp%10)
     sumn=sumn+a**length
     temp=temp//10
     length =length-1
if sumn == x:
    print("disarium number")
else :
    print("not a disarium number")
     
