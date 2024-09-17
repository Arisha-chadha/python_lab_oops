x = int(input("Enter number: "))
temp = x
sumd = 0
while temp != 0:
    a = temp % 10
    sumd += a  
    temp = temp // 10

if sumd != 0 and x % sumd == 0:
    print("Harshad number")
else:
    print("Not a Harshad number")

     
