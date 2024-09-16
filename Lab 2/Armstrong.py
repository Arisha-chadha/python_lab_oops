x=int(input("enter a no"))
ast=0
temp=x
length= len(str(x))
while temp>0:
      z=temp%10
      ast=ast+z**length
      temp=temp//10
if ast==x:
    print("yes number is a armstrong no")
else :
    print("number is not armstrong")
