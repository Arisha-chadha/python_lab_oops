n = int(input("enter number"))
r = int(input("enter number"))
#using C(n,r) = n! / r! * (n-r) !
factn= 1
i = 1
while i<=n:
  factn= i*factn
  i = i+1

numerator = factn         # n!
sub = n - r               # (n-r)
fact = 1
i = 1
while i<=sub:
  fact = i*fact
  i = i+1
  
factr= 1
i = 1
while i<=r:
  factr= i*factr
  i = i+1
denominator = fact    *factr    # (n-r)!
nCr= numerator/denominator

print("\nnCr =", nCr)
