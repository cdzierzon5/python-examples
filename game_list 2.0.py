
game_list=[]
while True:
    option = int(input("""
    1 - add a game to our list
    2 - remove a game from our list
    3 - insert a game into our list
    4 - exit
    """))
    if option == 1:
        game = input("what game would you like to add to your list?")
        game_list.append(game)
        print(game_list)
    elif option == 2:
        game = input("what game would you like to remove from your list?")
        print(game_list)
        while True:
            if game in game_list:
                q=input("are you sure you want to remove this game? "+ game)
                if q == "yes":
                    game_list.remove(game)
                    print(game_list)
                    break
                else:
                    print("then why did you choose option 2 YOU LOSER!!!")
            else:
                print(game+" is not in your list")
    elif option == 3:
        game = input("what game would you like to insert into your list")
        pos = int(input("at what position would you like to place "+ game+" in your list? "))
        pos -= 1

        while True:
            if pos < len(game_list):
                game_list.insert(pos,game)
                print(game_list)
                break
            else:
                print("invalid position")

    elif option == 4:
        input("press enter to exit")
        break
    else:
        print("that is not a good option")
