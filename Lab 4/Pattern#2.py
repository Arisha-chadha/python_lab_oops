#Pattern #2: Inverted Pyramid of Numbers
#Pattern:
#1 1 1 1 1 
# 2 2 2 2 
 # 3 3 3 
  # 4 4 
 #   5
for i in range(1, 6):
    for j in range(i-1):
        print(" ", end="")
    for j in range(5-i+1):
        print(i, end=" ")
    print() 
