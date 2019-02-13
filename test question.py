#Cody Dzierzon
#Test question

class Mail(object):
    """gives the values of the shipping information"""

    def __init__(self, name, address, number):
        self.name = name
        self.address = address
        self.number = number

name = "Bill"
address = "123 pear st"
number = "435-125-9874"
print("the shipping information of",name,"is",address,"and his number is",number)
    
             
