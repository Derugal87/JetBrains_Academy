import random


def main(game_score):
    user_name = input('Enter your name: ')
    print(f'Hello, {user_name}')
    game_count(user_name, game_score)


def game_count(user_name, game_score):
    with open('rating.txt', 'r') as file:
        for line in file:
            if user_name in line:
                game_score = int(line.split()[1])
                game_input(user_name, game_score)
            elif user_name not in line:
                game_input(user_name, game_score)


def game_input(user_name, game_score):
    user_option = input('')
    game_check(user_option, user_name, game_score)


def game_check(user_option, user_name, game_score):
    count = 0
    if user_option == '!rating':
        rating(user_name, game_score)
    elif user_option == '!exit':
        print('Bye!')
        exit(0)
    elif not user_option:
        print("Okay, let's start")
        choose_default(user_name, game_score)
    elif user_option:
        user_option = list(user_option.split(','))
        for i in user_option:
            count += 1
            if i in lose_pro.keys():
                if count == len(user_option):
                    print("Okay, let's start")
                    choose_pro(user_name, game_score, user_option)
            else:
                print('Invalid input')
                game_input(user_name, game_score)
    else:
        print('Invalid input')
        game_input(user_name, game_score)


def choose_default(user_name, game_score):
    user_choose = input('')
    if user_choose == 'back':
        print("Back to main menu")
        game_input(user_name, game_score)
    elif user_choose == '!exit':
        print('Bye!')
        exit(0)
    if user_choose == '!rating':
        rating(user_name, game_score)
    game_default(user_name, game_score, user_choose)


def game_default(user_name, game_score, user_choose):
    if user_choose in list(lose_default):
        comp_choose = random.choice(list(lose_default.values()))
        if user_choose == lose_default.get(comp_choose):
            game_score += 100
            print(f'Well done. The computer chose {comp_choose} and failed')
        elif user_choose == comp_choose:
            game_score += 50
            print(f'There is a draw ({user_choose})')
        else:
            print(f'Sorry, but the computer chose {comp_choose}')
        choose_default(user_name, game_score)
    else:
        print('Invalid input')
        choose_default(user_name, game_score)


def choose_pro(user_name, game_score, user_option):
    user_choose_pro = input('')
    if user_choose_pro == 'back':
        print("Back to main menu")
        game_input(user_name, game_score)
    elif user_choose_pro in user_option:
        game_pro(user_name, game_score, user_choose_pro, user_option)
    elif user_choose_pro == '!exit':
        print('Bye!')
        exit(0)
    if user_choose_pro == '!rating':
        rating(user_name, game_score)
    else:
        print('Invalid input')
        choose_pro(user_name, game_score, user_option)


def game_pro(user_name, game_score, user_choose_pro, user_option):
    comp_choose_pro = random.choice(user_option)
    for i in lose_pro.keys():
        if user_choose_pro in lose_pro[i] and comp_choose_pro == i:
            game_score += 100
            print(f'Well done. The computer chose {comp_choose_pro} and failed')
            choose_pro(user_name, game_score, user_option)
    if user_choose_pro == comp_choose_pro:
        game_score += 50
        print(f'There is a draw ({user_choose_pro})')
        choose_pro(user_name, game_score, user_option)
    else:
        print(f'Sorry, but the computer chose {comp_choose_pro}')
        choose_pro(user_name, game_score, user_option)


def rating(user_name, game_score):
    print(f'Your rating: {game_score}')
    game_input(user_name, game_score)


score = 0

lose_default = {
    'scissors': 'rock',
    'rock': 'paper',
    'paper': 'scissors'
}

lose_pro = {
    'rock': ['paper', 'air', 'water', 'dragon', 'devil', 'lightning', 'gun'],
    'fire': ['air', 'water', 'dragon', 'devil', 'lightning', 'gun', 'rock'],
    'scissors': ['water', 'dragon', 'devil', 'lightning', 'gun', 'rock', 'fire'],
    'snake': ['dragon', 'devil', 'lightning', 'gun', 'rock', 'fire', 'scissors'],
    'human': ['devil', 'lightning', 'gun', 'rock', 'fire', 'scissors', 'snake'],
    'tree': ['lightning', 'gun', 'rock', 'fire', 'scissors', 'snake', 'human'],
    'wolf': ['gun', 'rock', 'fire', 'scissors', 'snake', 'human', 'tree'],
    'sponge': ['rock', 'fire', 'scissors', 'snake', 'human', 'tree', 'wolf'],
    'paper': ['fire', 'scissors', 'snake', 'human', 'tree', 'wolf', 'sponge'],
    'air': ['scissors', 'snake', 'human', 'tree', 'wolf', 'sponge', 'paper'],
    'water': ['snake', 'human', 'tree', 'wolf', 'sponge', 'paper', 'air'],
    'dragon': ['human', 'tree', 'wolf', 'sponge', 'paper', 'air', 'water'],
    'devil': ['tree', 'wolf', 'sponge', 'paper', 'air', 'water', 'dragon'],
    'lightning': ['wolf', 'sponge', 'paper', 'air', 'water', 'dragon', 'devil'],
    'gun': ['sponge', 'paper', 'air', 'water', 'dragon', 'devil', 'lightning'],
}

main(score)
