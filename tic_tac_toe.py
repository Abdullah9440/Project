board = [" "] * 9

def display_board(): 
    print(f"""
 {board[0]} | {board[1]} | {board[2]}
---+---+---
 {board[3]} | {board[4]} | {board[5]}
---+---+---
 {board[6]} | {board[7]} | {board[8]}
""")
    
winning_check = [
    (0,1,2),
    (3,4,5),
    (6,7,8),

    (0,3,6),
    (1,4,7),
    (2,5,8),

    (0,4,8),
    (2,4,6)
]

player = 'X'
while True:
    display_board()
    try :
      position = int(input(f'enter index position between(0-8) for {player} :'))
      if position < 0 or position > 8:
          print('enter position between 0-8')
          continue
      if  board[position] != " ":
        print('the position is occupaied')
        continue
      board[position] = player
    
    
    except ValueError:
        print('invalid input')
        continue
    
    
    
    for a, b, c in winning_check:

        if board[a] == player and board[b] == player and board[c] == player:
            display_board()
            print(f"The winner is {player}")
            break
    if " " not in board:
            display_board()
            print('no empty position available,match draw')
            break
            
            
    if player == 'X':
        player = 'O'
    else:
        player = 'X'