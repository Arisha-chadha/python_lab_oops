n=int(input("enter a no"))
n1=0
n2=1
nx=n2
count=1
while count<=n:
    print(nx,end=" ")
    count+=1
    n1,n2=n2,nx
    nx=n1+n2
    print()
