import os
import random

clear = lambda: os.system('cls')

board = list(range(0, 9))


cells = 3
dashes = 13
spaces = 14




print('ВСЕМ OKAY, X O ')


def take_input(player_token):
    is_valid = False

    while not is_valid:
        if player_token == 'O':
            player_answer = random.randint(0, 8)
        else:
            player_answer = input(f"Куда поставить {player_token}?")
        try:
            player_answer = int(player_answer)
        except:
            print('Неправильный ввод. Нужно ввести число!')
            continue
        if 0 <= player_answer <= 8:
            if str(board[player_answer]) not in 'XO':
                board[player_answer] = player_token
                is_valid = True
            else:
                print("Клетка занята!")
                continue
    clear()

def display_board(brd):
    for i in range(cells):
        print(" " * spaces, end='')
        print("-" * dashes)
        print(" " * spaces, end='')
        print(f"| {board[i * 3]} | {board[i * 3 + 1]} | {board[i * 3 + 2]} |")
        print(" " * spaces, end='')
        print("-" * dashes)


def check_win():
    win_coords = (
        (0, 1, 2), (3, 4, 5), (6, 7, 8), (0, 3, 6),
        (1, 4, 7), (2, 5, 8), (0, 4, 8), (2, 4, 6)
    )
    for each in win_coords:
        if board[each[0]] == board[each[1]] == board[each[2]]:
            return board[each[0]]
    return False

def make_step(count):
    if count % 2 == 0:
        take_input('X')
    else:
        take_input('O')





def main():
    is_win = False
    counter = 0

    while not is_win:
        display_board(board)

        make_step(counter)
        counter += 1

        if counter > 4:
            winner = check_win()
            if winner:
                is_win = True
                print(f'{winner} победили!')
            elif counter == 9:
                print("Ничья!")
                break

    display_board(board)


main()











