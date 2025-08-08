words = []
with open('words.txt', 'r') as file:
    for line in file:
        words.append(line) # Add words from the current line to the main list

for item in words:
    print(item)