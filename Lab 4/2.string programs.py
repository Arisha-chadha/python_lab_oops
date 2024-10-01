#2.	Write a program to do the following
#A. To separate the following string into comma (,) separated values. X= “ India.is.my.country”
#B. To remove a given character from a string. Y=”M.A.N.I.P.A.L” 
#C. To remove the (.) dots from the above string.
#a. 
X = "India.is.my.country"
Xcs = X.replace('.', ',')
print("Comma separated string:", Xcs
#b. 
X = "M.A.N.I.P.A.L"
char= input("Enter the character to remove: ")
Xwithoutchar= X.replace(char, '')
print("String after removing the character:",Xwithoutchar)
#c. 
X= "M.A.N.I.P.A.L"
Xwithoutdot = X.replace('.', '')
print("String without dots:", Xwithoutdot)


