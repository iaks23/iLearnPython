print("Welcome to Horror House, tread carefully...\n")
print("Press 100 to stop playing iin case it gets too scary for you...\n")
choice = input("You're walking your dog, Rufus, and see an abandoned house. Do you: \n Explore (Press 7) \n Walk Away (Press 4) \n Let Rufus Decide (Press 10) \n")
ChoiceDict = {
    1: "The girl is angry. The broom handle whips out of your hands and lodges itself down yoour throat. You suffocate. You die.",
    2: "You ram the door bruising your shoulder but you're in! You want a weapon but there's not much around. Do you choose \n A Dusty Broom Handle (Press 16)  \n A Creepy Doll (Press 9) \n",
    3: "You hear a laugh from inside a room. Do you: \n Follow It (Press 16) \n Run Away (Press 14) \n",
    4: "Despite Rufus pulling towards the house, you return home. That night, he goes missing. Do you:\n Go looking for him inside the house (Press 7) \n Hope he comes home (Press 19) \n",
    5: "You run home, covered in Rufus' blood. You're alive, but at what cost? You dream of your dog every night, until the pain is too much for you to take...",
    6: "Rufus suddenly turns insane and starts attacking you. Do you: \n Stab him with a dagger (Press 5) \n Run (Press 13)",
    7: "The door is locked! Do you: \n Break A Window (Press 15) \n Barge in the door! (Press 2) \n",
    8: "As you turn to leave, Rufus slips away. You chase him around the side of the house and find an open cellar door, with steps leading down, Do you: \n Enter (Press 16) \n Grab him & leave for medical attention (Press 14)",
    9: "The doll starts to speak. Do you \n Try to figure out what she says (Press 11) \n Throw her on the floor in fear \n (Press 20)",
    10: "Rufus pulls towards the house, looks like you're going in (Press 7 to continue) \n",
    11: "The doll is asking you to go into a different room. Do you \n Agree and go (Press 16) \n Refuse and smash her on the floor (Press 20) \n",
    12: "Feeling scared, you want a weapon, Do you choose: \n A dusty broom handle (Press 3) \n A ceremmonial dagger (Press 6) \n",
    13: "Rufus is much faster than you. He manages to catch you with his teeth, you bleed out. You die.",
    14: "You get halfway down te driveway before you pass out from blood loss, nobody could save you in time.",
    15: "There are no rocks nearby, so you wrap your arm in your sweater and punch the window. It breaks but you've cut yourself. Do you: \n Leave and get medical attention (Press 8) \n Continue (Press 12)",
    16: "A young girl appears. Do you: \n Try to befriend her (Press 18) \n Hit her with a broom handle (Press 1) \n",
    17: "Rufus attacks you in your sleep. Your jugular bitten, you bleed to death.",
    18: "The young girl tries to take your hand and lead yoou away, Do you: \n Go with her (Press 20) \n Refuse and stay where you are. (Press 1) \n",
    19: "After waiting for 3 days, Rufus finally returns but doesn't seem like himself. Do you \n Ignore it. Happy he's home. (Press 17) \n Take him to the house to try and figure out why (Press 7)\n",
    20: "Ghosts appear. You fall to the floor and cannot move. Eventually, you die of dehydration, surrounded only by apparitions."
}
endgame = [1, 5, 13, 14, 17, 20, 100]

while(choice not in endgame):
    print(ChoiceDict.get(choice))
    choice = input()
    ChoiceDict.get(choice)

    if choice == 100:
        print("Sad to see you go. The house will be waiting for you.")
    
    elif choice == 20:
        print(ChoiceDict.get(20))
    
    elif choice == 1:
        print(ChoiceDict.get(1))
        
    elif choice == 5:
        print(ChoiceDict.get(5))

    elif choice == 13:
        print(ChoiceDict.get(13))

    elif choice == 14:
        print(ChoiceDict.get(14))

    elif choice == 17:
        print(ChoiceDict.get(17))
    
    else:
        print("Invalid choice!")
    
    









