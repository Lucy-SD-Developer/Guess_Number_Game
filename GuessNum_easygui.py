import easygui
import random
import sys

num = random.randint(1, 99)
count = 0
choice = easygui.ynbox('Would you like to play a guess number game?','A small Game')
if not choice:
    easygui.msgbox('Bye-bye!','Exit')
    sys.exit()
while count < 10:
    count += 1
    guess = easygui.integerbox('Input a number: ', 'Guess a number', None, 1, 99)
    if not guess:
        count -= 1
        continue      
    if guess == num:
        easygui.msgbox('You Win!','Winner')
        easygui.msgbox(f'You did it in {count} guesses!','Win Info')
        sys.exit()
    if guess > num:
        output = 'Too high' 
    else:
        output = 'Too low'
    if not easygui.ynbox(output, 'Output', ('ok!', 'I am done.')):
        easygui.buttonbox('Are you sure?', 'exit', ['Yes, bye-bye!'])
        sys.exit()
easygui.msgbox(f'You lose! Attempts over {count}. Please try again.','Lose Game')
