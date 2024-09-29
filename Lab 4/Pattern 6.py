# Reverse Pyramid of Numbers
#         1 
#       2 1 
#     3 2 1 
#   4 3 2 1 
# 5 4 3 2 1 
n = 5  

for i in range(1, n+1):
    print(" " * (n - i) * 2, end="")
    for j in range(i, 0, -1):
        print(j, end=" ")
    print()
