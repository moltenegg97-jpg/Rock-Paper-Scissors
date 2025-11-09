import random
import logging

logger = logging
logger.basicConfig(level = logging.INFO) #изменить INFO на DEBUG для большей информации
moves = ['rock', 'paper', 'scissors']

def set_games_amount():
    amount_of_wins = 0 #необходимое изначальное значение, иначе придется делать 2 цикла
    while amount_of_wins <= 0: #для проверки правильности ввода от пользователя
        print('до скольки побед будем играть?')
        try: 
            amount_of_wins =  int(input())
            if amount_of_wins <= 0:
                print ('число должно быть больше 0')
        except ValueError: print('введите число')
    return amount_of_wins

    


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
    
def main(amount_of_wins):
    game_is_finished = False
    round = 1
    wins = 0 #максимальное кол-во побед одной из сторон
    player_wins = 0 #количество побед игрока
    pc_wins = 0 #количество побед компьютера
    
    while wins < amount_of_wins:
        print (f'round: {round}')
        player_move = player_turn()
        if player_move ==  'quit':
            print ('игра окончена')
            break
        pc_move = pc_turn()    
        game_is_finished, winner = check_winner(player_move, 'игрок', pc_move, 'компьютер')

        if winner == 'игрок':
            player_wins += 1
        if winner == 'компьютер':
            pc_wins += 1
        print (f' текущий счет {player_wins}:{pc_wins}')

        print (f'game is finished: {game_is_finished}')
        if game_is_finished == True:
            wins = max(player_wins, pc_wins)
            game_is_finished = False

        if wins == amount_of_wins:
            if player_wins == amount_of_wins:
                print ('В общем сете победил игрок')
            if pc_wins == amount_of_wins:
                print ('В общем сете победил компьютер')
        logger.debug (f'wins {wins}')
        round += 1
        logger.debug (f'в конце хода {round}')
        print ('-----------') #для визуального разделения игр

amount_of_wins = set_games_amount()
main(amount_of_wins)

