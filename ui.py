
#initializing UI components

# creating a board to have guesses
from unittest import case

new_word = []  # list to store the mutted guess with colors (list of letters)
new_wordlist = []  # list to store all guesses with colors(list of words)

def UI(guesslist, outputlist):
    for guess, output in zip(guesslist, outputlist):
        
         for i in range(len(guess)):
            # decoding each output in the output list into colours
            if guess=="":
                print("_") # if no guess print empty spaces
            else:
                letter= ""
                match output[i]:
                    case 0:
                        # colour the letter grey
                        letter += "\033[90m" + guess[i].upper()

                    case 1:
                        # colour the letter green
                        letter += "\033[32m" + guess[i].upper()

                    case 2:
                        # colour the letter yellow
                        letter += "\033[33m" + guess[i].upper()

            print(letter)  # join the letters to form the guess
            print(" ")  # space between letters
            new_word.append(letter)
         new_wordlist.append(new_word) #append mutted guesses to a list
