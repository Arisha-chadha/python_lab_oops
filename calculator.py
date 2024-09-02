print("1:add 2:sub 3:multipy 4:divide 5: exit")
 
while True :
    ch=int(input("enter choice" ))
    if(ch==1):
        a=int(input("enter no"))
        b=int(input("enter no"))
        add=a+b 
        print(add)
    elif(ch==2):
        a-int(input("enter no"))
        b=int(input("enter no"))
        sub=a-b
        print(sub)
    elif(ch==3):
        a=int(input("enter no"))
        b=int(input("enter no"))
        mul=a*b
        print(mul)
    elif(ch==4):
        a=int(input("enter no"))
        b+int(input("enter no"))
        div=a/b
        print(div)
    elif(ch==5):
       break
