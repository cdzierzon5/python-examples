#Cody Dzierzon
#10/12/18



##loops=0
##while True:
##    print("I have looped" ,loops, "times")
##    loops+=123
##    if loops>10000:
##        break


##count=0
##while count!=100:
##    count+=1
##    if count>700:
##        break
##    if count == 6 or count == 66 or count == 666:
##        continue
##    print(count)
##



print("Your lone hero is surrounded by a massive army of trolls.")
print("Their decaying green bodies stretch out, melting into the horizon.")
print("Your hero unsheathes his sword for the last fight of his life.\n")

health=10
trolls=0
damage=3


while health >= 0:
    trolls += 1
    health -= damage
    print("Your hero swings and deafeats an evil troll,"\
          "but takes", damage, "damage points.\n")



    print("Your hero fought valiantly and defeated", trolls,"trolls")
    print("But alas, your hero is no more.")
