import os
import random
import math


aleat = random.randrange(50)

try:
    
    game = input('Do you want to play ? ')
    assert game == 'yes' or game == 'no'
    capital = int(input('Enter your capital : '))
    assert capital > 0
    
    while game == 'yes':
        choice = int(input('Enter a number between 0 and 49 : '))
        assert  0 <= choice <= 49
        bet = int(input('Enter the money you bet : '))
        assert 1 <= bet <= capital
    
        if choice == aleat:
            capital += bet*2
            print('You won, you just earned: ', bet, '$ and now you have : ', capital, '$')
          
        elif choice != aleat and choice%2 == aleat%2:
            capital -= bet
            bet = 0.5*bet
            bet = math.ceil(bet)
            capital += bet
            print('You lose but you get the same colour, you just lost : ', bet, '$ and now you have : ', capital, '$')

        else:
            capital -= bet
            print('You lose, now you have : ', capital, '$')
            
        game = input('Do you want to play ? ')

except ValueError:
    print('Value not allowed')
except AssertionError:
    print('Answer seriously')

#os.system('pause')
