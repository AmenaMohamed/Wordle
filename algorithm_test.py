#constant
N= 4
word=input("word:")
output=[0]*N
guess=input("guess:")
R=[0]*N

for i in range(N):
    R[i]= guess.count(word[i]) 
    #count the repeation of each letter , assign it to it's index 

for i in range(N):
    if word.find(guess[i])== -1 :
        output[i]= 0 #not found
    elif word.find(guess[i])== i :
        output[i] = 1 #found in correct pos
    elif R[i]!= 0:
        output[i] = 2 #found in incorrect pos
        R[i]-=1 # we found one of the repeations & coded it

print(output)