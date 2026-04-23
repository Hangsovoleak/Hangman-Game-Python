import random
import time

# Initial steps to invite in the game:
print("\nWELCOME TO HANGMAN GAME BY VOLEAK\n")

name = input("Enter your name: ")
print("Hello " + name + "! Best of Luck")

time.sleep(2)
print("The game is about to start!\n Let's play Hangman!!")
time.sleep(3)

# The parameters we require to execute the game:
def main():
    global count
    global display
    global word
    global already_guessed
    global length
    global play_game 
    global limit
    
    words_to_guess = ["january", "border", "image", "film", "promise", "kids", "lungs", "doll", "rhyme", "damage", "plants"]

    word = random.choice(words_to_guess)
    length = len(word)
    count = 0
    display = '_ ' * length
    already_guessed = []
    play_game = ""
    limit = 5

def play_loop():
    global play_game

    while True:
        play_game = input("Do You Want To Play Again? (y-yes, n-no): ").lower()
        if play_game == "y":
            main()
            hangman()
        elif play_game == "n":
            print("Thank For Playing! We expect you back again!")
            exit()
        else:
            print("Invalid input. Please enter y or n.\n")
        
def hangman():
    global count
    global display
    global word
    
    guess = input("This is the Hangman Word: " + display + "Enter your guess: \n")
    
    guess = guess.strip().lower()
    
    if len(guess) != 1 or not guess.isalpha():
        print("Invalid Input, Try a letter\n")
        hangman()
        return
    elif guess in already_guessed:
        print("Try another letter.\n")
        hangman()
        return
    elif guess in word:
        already_guessed.append(guess)
        
        new_display = ""
        for i in range(len(word)):
            if word[i] == guess:
                new_display += guess
            else:
                new_display += display[i]
        
        display = new_display
        print(display + "\n")
    else:
        count += 1
        
        if count == 1:
            time.sleep(1)
            print(" _____ \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  "_|___\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 2:
            time.sleep(1)
            print(" _____ \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  "_|___\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 3:
            time.sleep(1)
            print(" _____ \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  "_|___\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 4:
            time.sleep(1)
            print(" _____ \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  "_|___\n")
            print("Wrong guess. " + str(limit - count) + " guesses remaining\n")
        elif count == 5:
            time.sleep(1)
            print(" _____ \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  " | \n"
                  "_|___\n")
            print("Wrong guess. You are hanged!!!\n")
            
            print("The word was:", word)
            play_loop()
            return
                
    if display == word:
        print("Congrats! You have guessed the word correctly!")
        play_loop()
        return

    elif count != limit:
        hangman()
    
main()
hangman()   