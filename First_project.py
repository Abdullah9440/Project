#number guessing game
import random

number = random.randint(1,100)
while True:
 guess = int(input('enter your guess between 1 to 100 : '))
 if guess < number:
        print('low guess')
 elif guess > number:
        print('high guesss')
 else:
       print('currect guess')
       break

        
    
    