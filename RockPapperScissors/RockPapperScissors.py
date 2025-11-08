import random
import logging

logger = logging
logger.basicConfig(level = logging.INFO) #изменить INFO на DEBUG для большей информации
moves = ['rock', 'paper', 'scissors']

game_is_finished = False

wins = 0 #максимальное кол-во побед одной из сторон
player_wins = 0 #количество побед игрока
pc_wins = 0 #количество побед компьютера

while True: #для проверки правильности ввода от пользователя
    print('до скольки побед будем играть?')
    try: 
        amount_of_wins =  int(input())
        break
    except ValueError: print('введите число')
    


def check_winner(player1_move, player1, player2_move, player2):
    made_moves = {
        player1_move: player1,
        player2_move: player2
    }
    if 'paper' in made_moves and 'rock' in made_moves:
        print (f' победил {made_moves['paper']}')
        return True, made_moves['paper']
    if 'rock' in made_moves and 'scissors' in made_moves:
        print (f' победил {made_moves['rock']}')
        return True, made_moves['rock']
    if 'paper' in made_moves and 'scissors' in made_moves:
        print (f' победил {made_moves['scissors']}')
        return True, made_moves['scissors']
    if player1_move == player2_move:
        print ('ничья')
        return False, None

def player_turn():
    print ('Игрок 1 введите rock, paper, scissors or quit для того чтобы выйти')
    player_move = input(str).lower()
    while player_move not in moves and player_move != 'quit':
        print ('неверный ход')
        player_move = input(str) 
    print (f'игрок1 ввел {player_move}')
    return player_move

def pc_turn():
    pc_move = random.choice(moves)
    print (f'компьютер ввел {pc_move}')
    return pc_move
    

while game_is_finished == False and wins < amount_of_wins:

    player_move = player_turn()
    if player_move ==  'quit':
        print ('игра окончена')
        break
    pc_move = pc_turn()    
    game_is_finished, winner = check_winner(player_move, 'игрок', pc_move, 'компьютер')

    if winner == 'игрок':
        player_wins = player_wins+1
    if winner == 'компьютер':
        pc_wins = pc_wins+1
    print (f' текущий счет {player_wins}:{pc_wins}')

    print (f'game is finished: {game_is_finished}')
    if game_is_finished == True:
        wins = max(pc_wins, pc_wins)
        game_is_finished = False
    
    logger.debug (f'wins {wins}')
    print ('-----------') #для визуального разделения игр


