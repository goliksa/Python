import random

board = []

def board_drow():
    global board
    board = [['- ', '1 ', '2 ', '3 ', '4 ', '5 ']]
    letters = ['-  ', 'a  ', 'b  ', 'c  ', 'd  ', 'e  ']
    
    for g in range(5):
        board.append(['O'] * 6)

    for m in range(6):
        board[m][0] = letters[m]
        print(' '.join(board[m]))
    
def user_guess (ship_row, ship_col):
    attempt = 13
      
    while attempt != 0:
        print('How do you think, where is my ship? You have '+ str(attempt )+ ' attempt.')
        user_row = input('Enter row letter: ')
        
        if user_row == 'a' or  user_row == 'A':
            user_row = 1
        elif user_row == 'b' or user_row == 'B':
            user_row = 2
        elif user_row == 'c' or user_row == 'C':
            user_row = 3
        elif user_row == 'd' or user_row == 'D':
            user_row = 4
        elif user_row == 'e' or user_row == 'E':
            user_row = 5
        else:
            print('Your row guess out of our sea!')
            attempt -= 1
            continue

        user_col = input('Enter col number: ')   
        if user_col not in ['1', '2', '3', '4', '5']:
            print('Your col guess out of our sea!')
            user_col = 0
        else:
            if user_row == ship_row and int(user_col) == ship_col:
                    print('Huraaaaaaa!!! You win!!!')
 #                   win += 1
 #                   board_guess_drow(user_row, user_col, 'V' )
                    print()
                    play_again(ship_row, ship_col)
                    break                   
            else:            
                print('No! This is not my ship plase!. You may try again.')
                board_guess_drow(user_row, user_col, 'X')
                
        attempt -= 1

    print()
    print('Game over!')
    play_again(ship_row, ship_col)

def board_guess_drow(row, col,  chek):
    board[int(row)][int(col)] = chek
    for m in range(6):
        print(' '.join(board[m]))

def start():
    ship_row = random.randint(1, 5)
    ship_col = random.randint(1, 5)
    print('ship row: ' + str(ship_row))
    print('ship col: ' + str(ship_col))

    
    print('Before we start I\'d like to sorry for my English, it\'s not perfect! :)')
    print('Let\'s play "Super BattleShip" game!')
    print('Here is a 5x5 sea board')
    print()
    board_drow()
    print()
    user_guess(ship_row, ship_col)

def play_again(ship_row, ship_col):
    print('My ship was here: ')
    board_guess_drow(ship_row, ship_col, 'V')
    print('Do you want to play again? (Y - "Yes"; N - "No")')
    play_againe = input()
    if play_againe == 'Y':
        start()
    else:
        print('Good by!')
                        
#    lose += 1

start()

