#16 Equilateral Triangle with Stars (Asterisk Symbol)

#            * 
#          * *   
#          * * *   
#         * * * *   
#        * * * * *   
#       * * * * * *   
#      * * * * * * *
n = 7
for i in range(1, n + 1):
    for j in range(n - i):
        print(" ", end=' ')
    for j in range(i):
        print("*", end=' ')
    print()
