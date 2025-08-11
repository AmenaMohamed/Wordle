from main import words , word
import sys
from logic import compare
from ui import UI

#input the user guess "6 attempts = 6 iterations"

word= word.lower()
guesslist= []
outputlist= []

for i in range(6):
    guess=input("type in a word:").lower() #input from the GUI
    
    if len(guess) < len(word):
        print("too small!")# handling user errors
        continue

    elif len(guess) > len(word):
        print("too long!")# handling user errors
        continue
    else:
        guesslist.append(guess)# add this new guess to the list
        if guess not in words:
            print("word not found")
            continue
           # if correct -> you won! "on the UI", break
        elif word == guess:
            print("you won!") 
            sys.exit()  #finish the program
        else:
            output = compare(word,guess) # storing the encoded list
            outputlist.append[output] 
            #for each guess[] there is an output[] with the same index
            #guesslist[0:6] -> outputlist[0:6]
    UI(guesslist, outputlist)
