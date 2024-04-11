place = input("Choose a place: forest or cave? ")

if place == "forest":
    action = input("climb a tree or cross a river?")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action == "cross a river":
        print("You found a boat!")
    else:
        pass
elif place == "cave":
    print("You find a hidden treasure!") 
    action = input('continue in the dark or go with a torch?')
    if action == ('continue in the dark'):
        print ('why would you do that, you just fell into a deep hole')
    elif action == ('go with a torch'):
        print ('you survived, your now a millionaire and get all  the women, what comes next in your fate??? find out in our DLC for only  59.99$, (constant internet required)')
    else:
        pass    
else:
    pass