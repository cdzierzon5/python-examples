#Cody Dzierzon
#9/17/18
import math
def pythagreon_theorem(ap,bp):
    a=float(ap)
    b=float(bp)
    c=a*a+b*b
    c=math.sqrt(c)

    print("the third side is",c)





ai=input("enter the first side of the triangle")
bi=input("enter the second side of the triangle")
pythagreon_theorem(ai,bi)    
