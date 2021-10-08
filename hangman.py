import random
from hangman_words import word_list # here to import a list from other file 
from hangman_art import logo
from hangman_art import stages

print(logo)



#choose random word from imported list 
choosen_word = random.choice(word_list)
length = len(choosen_word)

print("the word have " + str(length) + " letters")


blank_list=[]


def main():
    
    lives = 6
    blanks()
    start_game = True

    while start_game:
        letter = prompt_user() #function that prompt user for letter and store in variable 
  
        check = check_letter(letter) #taking return value 0f prompt user and givving it as argument of check to check if the letter is there And return a list 
        result = ''.join(check)
        print(result)

        
        if not "-" in check:#checking in there blank we continue if there is no more blanks means player won game and we exit 
            print("finished the game")
            end_game = False
            start_game = end_game
        elif (letter not in choosen_word): #calculating lifes if he gave the wrong letter 
            stage =stages[lives]
            print(stage)
            lives -=1
            if lives == 0 :
                print(stages[lives])
                print("Game Over you lost, you have 6 wrong letters ")
                print("the word was " + choosen_word)
                return
            else:
                print("Wrong Guess")

        else:
            print("Correct Guess" )
  

#Prompt the user to enter and only accept one letter
def prompt_user():
    while True:
        guess_letter = input(f"\n Please give me a letter ? ").lower()
        if(len(guess_letter) == 1):
            return guess_letter
        elif(len(guess_letter) >=2):
            print("You have wrote more than one letter")
        return guess_letter

#checking letter if correct it is take arugment return of function prompt_user (that is guess letter that user give )
def check_letter (letter):

    for i in range (len(choosen_word)):
        if letter == choosen_word[i]:
            blank_list[i] = letter

    
    
    return blank_list
   
#creating the blanks 
def blanks ():


    for i in range (len(choosen_word)):
        blank_list.append("-")

    r =''.join(blank_list)
    
    print(r)

#Life calculation 

def life(letter, lives):
    if letter not in choosen_word:
        lives




    
main()


