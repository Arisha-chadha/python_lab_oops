n1 = int(input("enter no"))
n2= int(input("enter no"))
a = n1
b = n2
while b!=0:
    temp = b
    b = a%b
    a = temp

hcf = a
lcm = int((n1*n2)/hcf)

print("\nLCM  = ", lcm)
print("GCD = ", hcf)
