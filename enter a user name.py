###Cody Dzierzon
###9/13/18
##
###get a users name
##def get_name():
##    
###step 1 ask user for name
## name=input("what's your name?")
###step 2 display name
## print("the name yo u entered was:",name)
###step 3 verify the name
## input("is this correct? yes or no:")
##
##print("this is our function")
##get_name()

#calculate the area of the circle
#radius*radius*pi
def areaOfCircle():
 pi=3.14159265358979
#1get a radius
 radius= input("what is the radius:")
#2 calculate the area
 radius= float(radius)
 area= radius*radius*pi
#3 display the area
 print("the area of the circle is:",area)

areaOfCircle()
