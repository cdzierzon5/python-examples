#Cody Dzierzon
#10-12

import random

win = 0
pHealth = 100
mHealth = 800
print("Your lone hero is surrounded by a massive army of trolls.")
print("Their decaying green bodies stretch out, melting into the horizon.")
print("Your hero unsheathes his sword for the last fight of his life.\n")

choice= input("fight or run")

while choice == "fight":
    pDamage = random.randrange(0,400)
    print("You attack the trolls and did", pDamage,"damage")
    mHealth -= pDamage
    if mHealth > 0:
        mDamage = random.randrange(0,60)
        print("The trolls fight back doing", mDamage,"damage")
        pHealth -= mDamage
    if pHealth <=0:
        print("you have died")
        win=0
        break
    elif mHealth <=0:
        print("you have killed all of the trolls")
        win=1
        break
    elif pHealth >=0 and mHealth >=0:
        print("you have,", pHealth,"health")
        print("the trolls have", mHealth,"health")
        choice = input("fight or run")
        if choice == "fight":
            print("you attack again")
        elif choice == "run":
            break

if choice == "run":
    print("you are a coward")
if win == 0:
    print("game over")
else:
    print("you have won with,",pHealth,"health left")
