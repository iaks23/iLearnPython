import random

def get_movie():
    movie = random.choice(["Argo","Alien","Jumanji","Frozen","Hancock","Scream","Skyfall","Gravity","Cinderella","Inception","Interstellar","Ratatouille","Disturbia","Transformers","Divergent","Up","Aladdin","Flatliners","Oculus","Spiderman","Batman","Superman","Jaws","Twilight","Psycho"])
    return movie.upper()

def hangman(word):
    tries = 10
    validchars= 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
    guessed_letters = ''
    
    while tries > 0:
        word_completion = ""
        for char in word:
            if char in guessed_letters:
                word_completion += char
            else:
                word_completion = word_completion + "_" + " "
        
        if word_completion == word:
            print(word_completion)
            print("You win! Time for some netflix?")
            print("\n")
            break
        print("Guess the movie:", word_completion)
        print("\n")
        guess = input().upper()
        
        if guess in validchars and guess not in guessed_letters:
            guessed_letters += guess
        
        elif guess in guessed_letters:
            print("You've already tried that letter! Try another one.")
            print("\n")
        
        else:
            print("Enter a valid char")
            guess = input().upper()
        
        if guess not in word:
            tries -= 1
        
        if tries == 9:
            print("9 turns left")
            print("  --------  ")
            print("\n")
        if tries == 8:
            print("8 turns left")
            print("  ---------  ")
            print("Uh oh, you can see his head and he does not look happy.")
            print("      O      ")
            print("\n")
        if tries == 7:
            print("7 turns left")
            print("  ---------  ")
            print("      O      ")
            print("      |      ")
            print("\n")
        if tries == 6:
            print("6 turns left")
            print("  ---------  ")
            print("      O      ")
            print("      |      ")
            print("     /       ")
            print("\n")
        if tries == 5:
            print("5 turns left")
            print("  ---------  ")
            print("      O      ")
            print("      |      ")
            print("     / \     ")
            print("\n")
        if tries == 4:
            print("4 turns left")
            print("  ---------  ")
            print("    \ O      ")
            print("      |      ")
            print("     / \     ")
            print("\n")
        if tries == 3:
            print("3 turns left. Play carefully.")
            print("  ---------  ")
            print("    \ O /    ")
            print("      |      ")
            print("     / \     ")
            print("\n")
        if tries == 2:
            print("2 turns left")
            print("  ---------  ")
            print("    \ O /|   ")
            print("      |      ")
            print("     / \     ")
            print("\n")
        if tries == 1:
            print("Last turn, make sure to get it right!")
            print("  ---------  ")
            print("    \ O_|/   ")
            print("      |      ")
            print("     / \     ")  
            print("\n")
        if tries == 0:
            print("You lose :(, the correct answer was,",word)
            print("You let an innocent man die")
            print("  ---------  ")
            print("      O_|    ")
            print("     /|\     ")
            print("     / \     ")
            print("\n")
            break

def play():
    print("Welcome to Hangman! Try to guess the movie in 10 attempts!")
    movie = get_movie()
    hangman(movie)
    while input("Play again? Y/N ").upper() == "Y":
        print("\n")
        print("Welcome to Hangman! Try to guess the movie in 10 attempts!")
        movie = get_movie()
        hangman(movie)
        

play()