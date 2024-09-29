#13 Pyramid of Horizontal Tables
#0  
#0 1  
#0 2 4  
#0 3 6 9  
#0 4 8 12 16  
#0 5 10 15 20 25  
#0 6 12 18 24 30 36
n = 7
for i in range(n):
    for j in range(i + 1):
        print(i * j, end=' ')
    print()
