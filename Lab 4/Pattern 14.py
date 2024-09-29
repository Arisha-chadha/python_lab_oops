#14Pyramid Pattern of Alternate Numbers
#1 
#3 3 
#5 5 5 
#7 7 7 7 
#9 9 9 9 9
n = 5
num = 1
for i in range(1, n + 1):
    for j in range(i):
        print(num, end=' ')
    print()
    num += 2
