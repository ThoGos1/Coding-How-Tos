import random


print('This is a very simple rock-paper scissor game \nYou play against a random bot')

num = input('Enter the move you want to make: ')

ai = random.choice(['rock','paper','scissors'])

if(ai == num):
    print('Tie')
if(ai == 'rock' and num == 'scissors'):
    print('AI Wins')
if(ai == 'rock' and num == 'paper'):
    print('You Win')
if(ai == 'paper' and num == 'rock'):
    print('AI Wins')
if(ai == 'paper' and num == 'scissors'):
    print('You Win')
if(ai == 'scissors' and num == 'paper'):
    print('AI Wins')
if(ai == 'scissors' and num == 'rock'):
    print('You Win')



print('The AI chose:', ai)

