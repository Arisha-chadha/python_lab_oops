#Inverted Pyramid of Descending Numbers
#5 5 5 5 5 
#  4 4 4 4 
#   3 3 3 
#    2 2 
#      1
n = 5  
for i in range(n, 0, -1):
    print(" " * (n - i) * 2, end="")
    for j in range(1, i+1):
        print(i, end=" ")
    print()
