
#initializing UI components

# creating a board to have guesses
from unittest import case

new_word = []  # list to store the mutted guess with colors (list of letters)
new_wordlist = []  # list to store all guesses with colors(list of words)

def UI(guesslist, outputlist):
    for guess, output in zip(guesslist, outputlist):

         for i in range(len(guess)):
            # decoding each output in the output list into colours

            match output[i]:
                case 0:
                    # colour the letter grey
                       
                case 1:
                    # colour the letter green
                        
                case 2:
                    # colour the letter yellow
                        

            print(letter)  # join the letters to form the guess

