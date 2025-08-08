from main import words , word
import sys
from logic import compare

#input the user guess "6 attempts = 6 iterations"
# handling user errors

word= word.lower()

for i in range(6):
    guess=input("type in a word:").lower() #input from the GUI
    
    if len(guess) < len(word):
        print("too small!")
    else:

        if guess.found(words)== -1:
            print("word not found")
            i-=1
           # if correct -> you won! "on the GUI", break
        elif word == guess:
            print("you won!") 
            sys.exit()  #finish the program
        else:
            output = compare(word,guess) # storing the encoded list


