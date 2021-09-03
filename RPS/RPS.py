import random

def play(plays):
    playlist = ['ROCK','PAPER','SCISSORS']
    i = 0
    uscore = 0
    cscore = 0
    while (i < plays):
        user = input("Take your pick! Rock, Paper, or Scissors? ")
        user = user.upper()
        comp = random.choice(playlist)
        
        if(user==comp):
            print('User played: '+user +" Comp played: "+comp)
            print('It is a tie!')
        
        elif(user=='ROCK'):
            if(comp=='SCISSORS'):
                print('User played: '+user +" Comp played: "+comp)
                print('You win!')
                uscore +=1
            else:
                print('User played: '+user +" Comp played: "+comp)
                print('You lose :(')
                cscore +=1
        
        elif(user=='PAPER'):
            if(comp=='ROCK'):
                print('User played: '+user +" Comp played: "+comp)
                print('You win!')
                uscore +=1
            else:
                print('User played: '+user +" Comp played: "+comp)
                print('You lose :(')
                cscore +=1
        
        elif(user=='SCISSORS'):
            if(comp=='PAPER'):
                print('User played: '+user +" Comp played: "+comp)
                print('You win!')
                uscore +=1
            else:
                print('User played: '+user +" Comp played: "+comp)
                print('You lose :(')
                cscore +=1
        
        else:
            
            print('Invalid play, please type in a valid input!')
            
            return False
        
        
        i += 1
        
        
        
   
    print('Computer Total: '+ str(cscore))
    print('User Total: '+ str(uscore))
    
    if(cscore > uscore):
        result = 'Computer wins! Better luck next time.'
    
    elif(cscore < uscore):
        result = 'Congratulations! You win!'
    
    else:
        result = 'The game is tied. We are all winners here.'
    
        
    return result



num = int(input("Would you like to play a best of 1 or 3 or 5 match? "))
result = play(num)
print(result)