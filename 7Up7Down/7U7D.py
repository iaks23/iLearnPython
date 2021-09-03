import random


def gamble(guess,min,max):
    """This function tells if the user has won or lost"""
    d1 = random.randint(min,max)
    d2 = random.randint(min,max)
    total = d1+d2
    
    if(total > 7 and guess == "7U"):
        print("The die 1 says:"+str(d1))
        print("The die 2 says:"+str(d2))
        print("The total was "+str(total) + " You won! :D")
        return True
    elif(total < 7 and guess == "7D"):
        print("The die 1 says:"+str(d1))
        print("The die 2 says:"+str(d2))
        print("The total was "+str(total) + " You won! :D")
        return True
    elif(total == 7 and guess == "7E"):
        print("The die 1 says:"+str(d1))
        print("The die 2 says:"+str(d2))
        print("The total was "+str(total) + " You won! :D")
        return True
    else:
        print("The die 1 says:"+str(d1))
        print("The die 2 says:"+str(d2))
        print("The total was "+str(total) + " You lost :(")
        return False


min = 1
max = 6
option = input("7U, 7D, OR 7E? ")
gamble(option,min,max)