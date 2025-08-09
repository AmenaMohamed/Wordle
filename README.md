# Wordle game:

This game is based on inputing 5_letter word as a guess,
you keep trying words until reaching 6 attempts 
the game shows you correct letters you used in each word with green
, correct letters but in incorrect position with yellow 
and incorrect letters with gray.

I divided this game into 3 files main.py , input.py , logic.py for easy read and mainapulation.

# main.py :contains the main program 
{importing words from txt file to words[], picking a random word}

# input.py :input data from the user
{it has the words[], the random word "word" passed to it , have the comparision between the user input & randomly picked one }

# logic.py: code logic of comparing 
{uses 0 ,1 ,2 to encode each letter of the user input word}

_______________________________________________________________________

# program works as follows :
1- importing words from txt file into "words[]" 
(using file reading commands) , then using "random" library to randomly choose a word from the list (main.py)

2- the randomly choosen word "word" and the list is passed to
 _input.py_
by "import" , by using loop of 6 iterations "6 attempts" , user input is handled (unreal /too long/too short  words) and stored in "guess" without skipping an attempt ,

 if the guess is the same as word then ,print won message & exit program , else compare two words "compare()"(imported from _logic.py_)


3- In _logic.py_ for each letter in word there is the number of it's repeation stored in R[] (list) 
ex: word = THESE , R=[1,1,2,1,2] using "word.count()" 
for each letter in guess there is an encoding (stored in "output[]")
(number resemples it's state)
ex: word = THESE , guess= HELLO by searching for each letter of HELLO in THESE.                        


     | number      |        state                 |    UI     |
     | :---------: | :--------------------------: | --------: |
     |     0       | wrong letter                 |   grey    |
     |     1       | correct let. in correct pos. |   green   |
     |     2       | correct let. in wrong   pos. |   yellow  |


        index= 0,1,2,3,4 (not a read list or though)
        word= [T,H,E,S,E]
        guess=[H,E,L,L,O]
we get output=[2,2,0,0,0]

that means that the H, E in HELLO are indeed present in THESE , but in wrong position , and rest of the letters are not present.


