#11 Connected Inverted Pyramid Pattern of Numbers
#5 4 3 2 1 1 2 3 4 5 
#5 4 3 2 2 3 4 5 
#5 4 3 3 4 5 
#5 4 4 5 
#5 5
n = 5  

for i in range(n):
    for j in range(n, i, -1):
        print(j, end=" ")
    for j in range(i+1, n+1):
        print(j, end=" ")
    print()  
