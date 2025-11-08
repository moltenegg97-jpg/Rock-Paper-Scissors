import random

moves = ['rock', 'paper', 'scissors']

game_is_finished = False


def check_moves(player1_move, player1, player2_move, player2):
    made_moves = {
        player1_move: player1,
        player2_move: player2
    }
    if 'paper' in made_moves and 'rock' in made_moves:
        print (f' победил {made_moves['paper']}')
        return True
    if 'rock' in made_moves and 'scissors' in made_moves:
        print (f' победил {made_moves['rock']}')
        return True
    if 'paper' in made_moves and 'scissors' in made_moves:
        print (f' победил {made_moves['scissors']}')
        return True
    if player1_move == player2_move:
        print ('ничья')
        return False
    
while game_is_finished == False:
    print ('Игрок 1 введите rock, paper, or scissors')
    player_move = input(str).lower()
    while player_move not in moves:
        print ('неверный ход')
        player_move = input(str) 
    print (f'игрок1 ввел {player_move}')

    pc_move = random.choice(moves)
    print (f'компьютер ввел {pc_move}')

    game_is_finished = check_moves(player_move, 'игрок', pc_move, 'компьютер')
