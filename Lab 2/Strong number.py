n=int(input("Enter a number:"))
sum=0
temp=n
while(n):
    i=1
    f=1
    r=n%10
    while(i<=r):
        f=f*i
        i=i+1
    sum=sum+f
    n=n//10
if(sum==temp):
    print("The number is a strong number")
else:
    print("The number is not a strong number")
