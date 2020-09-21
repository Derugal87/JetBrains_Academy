import random

some_list = ['python', 'java', 'kotlin', 'javascript']
chosen_word = random.choice(some_list)
let_out = []

def game():
    global mistakes
    mistakes = 0
    word = "-" * len(chosen_word)
    type = input('Type "play" to play the game, "exit" to quit: ')
    if type == 'play':
        print()
        print(word)
        while mistakes < 8:
            if '-' in word:
                symbol = input('Input a letter: ')
                if len(symbol) == 1:
                    if not symbol.isupper():
                        if symbol.isalpha():
                            if symbol in chosen_word:
                                symbol_count = chosen_word.count(symbol)
                                if symbol_count == 2:
                                    symbol_index_1 = chosen_word.index(symbol)
                                    symbol_index_2 = chosen_word.rindex(symbol)
                                    word = list(word)
                                    if word[symbol_index_1] == '-' and word[symbol_index_2] == '-':
                                        word[symbol_index_1] = symbol
                                        word[symbol_index_2] = word[symbol_index_1]
                                    else:
                                        print('You already typed this letter')
                                    word = ''.join(word)
                                    print()
                                    print(f'{word}')
                                else:
                                    symbol_index = chosen_word.index(symbol)
                                    word = list(word)
                                    if word[symbol_index] == '-':
                                        word[symbol_index] = symbol
                                        word = ''.join(word)
                                    else:
                                        print('You already typed this letter')
                                    word = ''.join(word)
                                    print()
                                    print(f'{word}')
                            else:
                                if symbol in let_out:
                                    print('You already typed this letter')
                                    print()
                                    print(f'{word}')
                                else:
                                    mistakes += 1
                                    if mistakes < 8:
                                        let_out.append(symbol)
                                        print('No such letter in the word\n')
                                        print(f'{word}')
                                    else:
                                        print('No such letter in the word')
                        else:
                            print('It is not an ASCII lowercase letter')
                            print()
                            print(f'{word}')
                    else:
                        print('It is not an ASCII lowercase letter')
                        print()
                        print(f'{word}')
                else:
                    print('You should input a single letter')
                    print()
                    print(f'{word}')
            else:
                print('You guessed the word!\n'
                      'You survived!')
                exit(0)
        else:
            print('You lost!')
            exit(0)
    elif type == 'exit':
        exit(0)
    else:
        game()
print('H A N G M A N')
game()