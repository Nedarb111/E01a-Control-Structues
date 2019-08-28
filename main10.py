#!/usr/bin/env python3

import sys, utils, random           # import the modules we will need

utils.check_version((3,7))          # make sure we are running at least Python 3.7
utils.clear()                       # clear the screen


print('Greetings!')                             #this types out greetings
colors = ['red','orange','yellow','green','blue','violet','purple']         #this tells the computer the sellection of colors that can be identified
play_again = ''                     #this establishes play_again as a code in the computer
best_count = sys.maxsize            # the biggest number
while (play_again != 'n' and play_again != 'no'):       #this makes it so that you can type in whether you want to play again or not and end the code. 
    match_color = random.choice(colors)         #this makes it so that the favoite color of the computer is randomly picked
    count = 0           #This establishes that the count starts at 0
    color = ''          #this establishes that color is the input
    while (color != match_color):           #this allows the code to keep going as long as it doesn't get the right answer.
        color = input("\nWhat is my favorite color? ")  #\n is a special code that adds a new line
        color = color.lower().strip()           #this is allowing any of the colors to be spelled in any select amount of ways
        count += 1              #Everytime time you guess it adds another number to the total count.
        if (color == match_color):          #This is establishing some code where it's saying "If" you get the right color it will give the resonce in the line bellow
            print('Correct!')               #This is what it tells you if you guess the color right
        else:                               #This is saying "if it's anything else" for the line bellow
            print('Sorry, try again. You have guessed {guesses} times.'.format(guesses=count)) #this makes it so that any color guessed wrong will give you this and tell you how many times you've guessed the wrong answer.
    print('\nYou guessed it in {0} tries!'.format(count))       #this prints out the responce that the line above it establishes.
    if (count < best_count):            #this is saying "if this happens" to the code bellow
        print('This was your best guess so far!')       #this will print out "this was your best guess so far!" if you get your lowest amount.
        best_count = count                              #this is overriding the other best counts that were established and makes sure that your best count is labeled as so.
    play_again = input("\nWould you like to play again? ").lower().strip()      #this is reussing the script from earlier to allow the player to type in whether he wants to play or not again.
print('Thanks for playing!')                    #this prints out "thanks for playing" if you sellected that you were done