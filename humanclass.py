class Human(object):

    def __init__(self, name, hair_color, eye_color, height, weight, iq, gender, race):
        self.name=name
        self.hair_color=hair_color
        self.eye_color=eye_color
        self.height=height
        self.weight=weight
        self.iq=iq
        self.gender=gender
        self.race=race
    def intro_self(self):
        print()
        print()
        print("hello my name is "+self.name)
    def describe_self(self):
        print()
        print()
        print("I have "+self.hair_color+" hair")
        print("I have " + self.eye_color + " eyes")
        print("I am " ,self.height ,"feet tall")
        print("I weigh " ,self.weight ," lbs")
        print("I am a " + self.race +" "+self.gender+" "+ "with an iq of " ,self.iq)
    def iq_self(self):
        print()
        print()
        print("your current iq is:", self.iq)
        q1 = input("what is the best sport in the world? ").lower()
        if q1 == "soccer":
            print("that is correct!!!")
            self.iq += 15
            print("your iq is now:",self.iq)
        else:
            print("sorry that is not correct")
    def BMI_self(self):
        print()
        print()
        print("Your BMI is based off your height:",self.height,"feet tall, and your weight:",self.weight,"lbs")
        kilo=self.weight * 0.453592
        meter=self.height * 0.3048
        meter2 = meter * meter
        bmi = kilo//meter2
        print("your bmi is:", bmi)
        if bmi > 30:
            print("You are obese")
        elif bmi > 25:
            print("you are overweight")
        elif bmi > 18:
            print("your BMI is normal/healthy")
        else:
            print("you are underweight")
cody = Human("Cody", "Blonde", "Blue", 6, 180, 112, "Male", "WHITE BOI")

bob = Human("Bob", "Green", "Black", 3, 111, 12, "Male", "Blob")

cody.intro_self()
cody.describe_self()
cody.iq_self()
cody.BMI_self()

# bob.intro_self()
# bob.describe_self()
# bob.iq_self()
# bob.BMI_self()

