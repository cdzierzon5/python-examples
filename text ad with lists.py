#Hero's Inventory
#Cody Dzierzon
#11-28-18
import os
import random
def hud():
    print("stats: ",player_stats)
    print("inventory: ",inventory)
    print("equiped: ",equiped)

chest_items = ["gold","gems","elven sword","bow","crossbow","coins","traps"]
player_health = 100
player_armor = 1250
player_attack = 250
player_money = 0
inventory = ["rusty sword","leather armor","wood sheild","small healing potion"]
max_inventory = 10
equiped = []
player_stats = ["health",player_health,"armor",player_armor,
           "attack",player_attack,"money",player_money]

print("As you start on your journey you have the following")
print("player stats: ")
print(player_stats)
print()
print("Your items include:")
for item in inventory:
    print(item)

input("\nPress the enter key to continue.")
os.system('cls')
hud()

print("You have", len(inventory),"/",max_inventory,"items in your possession.")
print("so you can pick up ", max_inventory-len(inventory), "more items")
input("\nPress the enter key to continue.")
os.system('cls')
hud()

print("you get attacked and take damage")
player_stats[1] -= 22
input("\nPress the enter key to continue.")
os.system('cls')
hud()

input("\nyou have take some damage on your journey \n" +
      "your health is at" + str(player_stats[1]) + "\n" +
      "you need to use your healing potion \nPress the enter key to continue.")

if "smal healing potion" in inventory:
    print("You will live to fight another day. by using the healing potion")
    player_stats[1] += 20
    inventory.remove("small healing potion")
input("\nPress the enter key to continue.")
os.system('cls')
hud()

for i in range(len(inventory)):
    print(str(i),inventory[i])
print("let's equip some armor")
index = int(input("\nEnter the index number for an armor item in your inventory you wish to equip "))

while index > len(inventory)-1 or index < 0 and index != "":
    print("that number is out of range")
    index = int (input("\nEnter the index number for and armor item in inventory."))
print("you equip your ", inventory[index])
equiped.append(inventory[index])
inventory.remove(inventory[index])
if "leather armor" in equiped:
    player_stats[3] += 1000
if "Wood shield" in equiped:
    player_stats[3] += 500
input("\nPress the enter key to continue.")
os.system('cls')
hud()

chest = []
for i in range(random.randrange(len(chest_items))):
    item = random.choice(chest_items)
    chest.append(item)

print("You fint a chest which contains:")
print(chest)
print()
print("You add the contents of the chest to your inventory.")

if len(inventory) + len(chest) < max_inventory:
    inventory += chest
else:
    drop = len(inventory) + len(chest) - max_inventory
    for i in range(drop):
        x=random.choice(chest)
        chest.remove(x)
    inventory += chest
input("\nPress the enter key to continue.")
os.system('cls')
hud()

print("convert treasure to gold")
if "gold" in inventory:
    player_stats[7]+=100
    inventory.remove("gold")
if "gems" in inventory:
    player_stats[7]+=1000
    inventory.remove("gems")
input("\nPress the enter key to continue.")
os.system('cls')
hud()

if player_stats[7] > 100:
    print("You want to trade your sword for a crossbow. so you sell your\n" +
          "sword for 20 gold and buy a crossbow for 100 gold")
    player_stats[7] += 20
    player_stats[7] -= 100
    inventory[0] = "crossbow"
input("\nPress the enter key to continue.")
os.system('cls')
hud()

print("You trade in the last 2 items from your inventory for a new item.")
inventory[len(inventory)-2:len(inventory)] = ["orb of future telling"]
input("\nPress the enter key to continue.")
os.system('cls')
hud()

print("In a great battle, your sheild is destoryed.")
for i in range(len(inventory)):
    if inventory[i] == "Wood shield":
        del inventory[i]
for i in range(len(equiped)):
    if  equiped[i] == "Wood shield":
        del equiped[i]
input("\nPress the enter key to continue.")
os.system('cls')
hud()

print("Your first 2 items in your inventory are stolen by thieves.")
del inventory[:2]
print("Your inventory is now:")
print(inventory)
input("\nPress the enter key to continue.")
os.system('cls')
hud()

input("\nPress the enter key to continue.")
