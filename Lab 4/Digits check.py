#Write a program to check if a string contains only digits. 

string = input("Enter a string: ")
if all(char.isdigit() for char in string):
    print("The string contains only digits.")
else:
    print("The string contains characters other than digits.")