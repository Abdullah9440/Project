#number guessing game
import random

number = random.randint(1,100)
while True:
       try:
              guess = int(input('enter your guess between 1 to 100 : '))
       except ValueError:
              print('enter valid number')
              continue
       if guess < number:
               print('low guess')
       elif guess > number:
               print('high guesss')
       else:
              print('currect guess')
              break
     
  
 

        
    
    