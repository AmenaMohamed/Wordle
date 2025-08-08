word=input("word:")
output =""
guess=input("guess:")
for i in word:
    if guess.find(word)==i:
        output[i]= 1 #found in correct pos
    elif guess.find(word)==-1 :
        output[i] = 0 #not found
    else: 
        output[i] = 2 #found in incorrect pos
print(output)