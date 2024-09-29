#12 Even Number Pyramid Pattern
#10 
#10 8 
#10 8 6 
#10 8 6 4 
#10 8 6 4 2
n = 5
for i in range(1, n+1):
    num = 10
    for j in range(i):
        print(num, end=' ')
        num -= 2
    print()
