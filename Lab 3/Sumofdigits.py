x = int(input("Enter number: "))
temp=x
sumd = 0
while temp != 0:
    a = temp % 10
    sumd += a  
    temp = temp // 10
print("sum of digits", sumd)
