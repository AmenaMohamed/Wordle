import random # for easier random choice from the list

from logic import compare

#import words to the code
words = []
with open('words.txt', 'r') as file:
    for line in file: #read each line from the txt file
        words.append(line.strip()) #add each line "word" to the words list


#randomly choose a word from the list "words[]"
word = random.choice(words)

print(word)

