
#initializing UI components

# creating a board to have guesses
from unittest import case


new_wordlist = []  # list to store all guesses with colors(list of words)

def UI(guesslist, outputlist):
    for guess, output in zip(guesslist, outputlist):
        
        
            # decoding each output in the output list into colours
        if guess=="":
            print("_ " * len(output)) # if no guess print empty spaces
        else:
            for i in range(len(guess)):
                new_word = []  # list to store the mutted guess with colors (list of letters)
                match output[i]:
                    case 0:
                        # colour the letter grey
                        new_word.append("\033[30m" + guess[i].upper())

                    case 1:
                        # colour the letter green
                        new_word.append("\033[32m" + guess[i].upper())


                    case 2:
                        # colour the letter yellow
                        new_word.append("\033[33m" + guess[i].upper())

        print(" ".join(new_word) + "\033[0m")

        new_wordlist.append(new_word) #append mutted guesses to a list
