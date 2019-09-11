# A Keanu Reeves dating sim text adventure
keanuAffection = 0
playerName = ""

def addAffection(x):
    global keanuAffection
    keanuAffection += x
    return keanuAffection

def subtractAffection(x):
    global keanuAffection
    keanuAffection -= x
    return keanuAffection

def checkAffection():
    if (keanuAffection >= 50):
        goodEnding()
    else:
        badEnding()

def badEnding():
    print("Keanu leaves and you never see him again.")
    exit()

def goodEnding():
    print("TODO")
    exit()

def intro():
    print("❣◕ ‿ ◕❣ Welcome to the Keanu Reeves dating simulator. ❣◕ ‿ ◕❣")
    global playerName
    playerName = input("> What's your name?  ")
    print("> You're sitting on a park bench, eating a sandwich and reading your favorite book. You're listening to music on your headphones.")
    music = input("> Who's your favorite artist? ")
    if(music != 'Nickelback'):
        print("> " + music +  "? Nice!")
    else:
        print("> Nickelback? Gross.")
        exit()
    print("> Someone sits next to you. You sneak a glance and are shocked to see Keanu Reeves, famous actor!")

def choice1():
    print("> 'Mind if I sit next to you?' he asks. You're flabbergasted. He's way more handsome in real life than in the movies.\nHis raven black hair gently frames his features. Salt and pepper stubble sprinkled across his jawline.\nBreathtaking.")
    print(">  Let Keanu sit next to you? [y/n]")
    sit = input("> ")
    if(sit == 'y'):
        addAffection(10)
        print("'Great!' Keanu says.")
    elif(sit == 'n'):
        subtractAffection(1000)
        checkAffection()

def choice2():
    print("You feel your face growing red. You've been watching his movies for years now. God, he's so handsome.")
    print("Suddenly, you're snapped out of your reverie. 'What's your name?' Keanu asks.")
    print("'Er, it's "  + playerName + ",' you reply. 'Really? That's a breathtaking name,' Keanu says.")
    print("What do you do? Select a number.")
    actions = ['Blush and shyly turn away','Reply with "You\'re pretty breathtaking yourself ;)"','Giggle and play with your hair','Scream']
    while True:
        try:
            playerAction = input("[1] " + actions[0] + "\n[2] " + actions[1] "\n[3] " + actions[2] "\n[4] " + actions[3])
        except ValueError:
            print("Please enter a valid response.")
            continue
        if input < 1 or input > 4:
            print("Please enter a valid response.")
            continue
        else:
            #Value successfully inputted. Breaking the loop
            break
    if playerAction == 1:
        addAffection(5)
        print("Keanu smiles at you.")
    if playerAction ==  2:
        addAffection(10)
        print("Keanu laughs.")
    if playerAction == 3:
        addAffection(5)
        print("Keanu smiles at you.")
    if playerAction == 4:
        subtractAffection(50)
        checkAffection()

intro()
choice1()
choice2()
