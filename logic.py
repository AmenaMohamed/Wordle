from main import word , guess
#constant
N= 4
output=[0]*N
R=[0]*N

def compare(word,guess):
    for i in range(N):
        R[i]= guess.count(word[i]) 
        #count the repeation of each letter , assign it to it's index 
    #encoding 
    for i in range(N):
        if word.find(guess[i])== -1 :
            output[i]= 0 #not found
        elif word.find(guess[i])== i :
            output[i] = 1 #found in correct pos
        elif R[i]!= 0:
            output[i] = 2 #found in incorrect pos
            R[i]-=1 # we found one of the repeations & encoded it

    return output

   # else -> compare the guess to randomly choosen word , 
   #      -> output the similarities "position" & "letters"
   #      -> 0_not a letter / 1 correct pos / 2 incorrect pos
   #      -> store the guess , view it on GUI
#if 6 attempts finished "i==0"-> you lost "on GUI"