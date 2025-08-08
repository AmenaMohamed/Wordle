import random # for easier random choice from the list
import sys
import logic

#import words to the code
words = []
with open('words.txt', 'r') as file:
    for line in file: #read each line from the txt file
        words.append(line) #add wordseach line "word" to the words list


#randomly choose a word from the list "words[]"
word = random.choice(words)

print(word)

#input the user guess "6 attempts = 6 iterations"
for i in range(6):
    guess=input("type in a word:") #input from the GUI
    if guess.found(words)== -1:
       print("word not found")
       i-=1
   # if correct -> you won! "on the GUI", break
    if word == guess:
       print("you won!") 
       sys.exit()  #finish the program
    else:
        output = compare(word,guess) # storing the encoded list

        

