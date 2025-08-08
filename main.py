import random # for easier random choice from the list


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
   # if correct -> you won! "on the GUI", break
    if word == guess:
       print("you won!")   #finish the program
    else:
   # else -> compare the guess to randomly choosen word , 
   #      -> output the similarities "position" & "letters"
   #      -> store the guess , view it on GUI
#if 6 attempts finished "i==0"-> you lost "on GUI"