start = '''
You are awaken by a loud scream outside. You stand up and go towards your window, you see what appears to be a fight between a woman and a man.
Should you go outside and intervene or mind your own business and stay inside?
'''

print(start)

print("Type 'outside' to intervene or 'inside' to mind your own business.")
user_input = input()
if user_input == "outside":
    print("You decided to go outside and intervene. As you move closer to the scene you realize that the woman is eating the man.")
    print("You step on a twig causing the woman to quickly run towards you.")
    print("You look around in search for a weapon and see a big rock and a thick stick")
    print("Type 'rock' to choose the rock or 'stick' to choose the stick.")
    weapon = input()
    if weapon == "rock":
        print("You chose the rock as your weapon.")
        print("You throw the rock at the woman, but you miss. She devours you and goes into your house killing your whole family.")
    elif weapon == "stick":
        print("You chose the stick as your weapon")
        print("You're able to stab the woman with the stick in her head")
        print("However, the man being attacked is now a zombie too, Your stick is not enough to fight him off.")
        print("He eats you.")

elif user_input == "inside":
    print("You choose to stay inside and mind you own business.")
    print("You feel thirsty, do you go down stairs and get a drink of water or do you go back to sleep.")
    print("Type 'water' if you want to go downstairs or 'sleep' to go back to bed")
    water = input()
    if water == "water":
        print("You chose to go get a glass of water.")
        print("While doing so, you see your dog come rushing in. Its eyes appear red and he has blood dripping from his mouth.")
        print("You get closer to him to check if he is okay, but before you get a chance to check, he attacks you.")
    elif water == "sleep":
        print("You chose to go back to sleep.")
        print("You wake up to find that the world is ending. The zombie apocalyse has started, will you survive?")    
