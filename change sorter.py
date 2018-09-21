#Cody Dzierzon
#9/21/18
# $_change sorter_$

def change():
    #1 get input from user find out how much change
    total_change = int(input("How much change do you have in your pocket, in cents: "))
    #2 calculate total for q n d p
    q = total_change//25
    whats_left=total_change%25
    d = whats_left/10
    whats_left=whats_left%10
    n = whats_left/5
    whats_left=whats_left%5
    p = whats_left
    #3 display it back to the user
    print("Quarters:",q,"\nDimes:",d,"\nNickles",n,"\nPennies",p)

##change()


def change2(total_change):
    #1 get input from user find out how much change
    total_chang = total_change
    #2 calculate total for q n d p
    dol = total_change//100
    whats_left = total_change%100
    q = whats_left//25
    whats_left=total_change%25
    d = whats_left/10
    whats_left=whats_left%10
    n = whats_left/5
    whats_left=whats_left%5
    p = whats_left
    return dol,q,d,n,p
    
total_change = int(input("How much change do you have in your pocket: "))
dol,q,d,n,p = change2(total_change)
#3 display it back to the user
print("$",dol,"\nQuarters:",q,"\nDimes:",d,"\nNickles",n,"\nPennies",p)
