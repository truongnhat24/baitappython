#!/usr/bin/env python3

from math import inf as infinity
from random import choice
import platform
import time
from os import system

HUMAN = -1
COMP = +1

def evaluate(state, player, chain_length):
    if wins(state, player, chain_length):
        return 1
    elif wins(state, -player, chain_length):
        return -1
    else:
        return 0

def wins(state, player, chain_length):
    rows = len(state)
    cols = len(state[0])
    
    # Check rows
    for i in range(rows):
        for j in range(cols - chain_length + 1):
            if all(state[i][j+k] == player for k in range(chain_length)):
                return True
    
    # Check columns
    for i in range(rows - chain_length + 1):
        for j in range(cols):
            if all(state[i+k][j] == player for k in range(chain_length)):
                return True
    
    # Check diagonals (\)
    for i in range(rows - chain_length + 1):
        for j in range(cols - chain_length + 1):
            if all(state[i+k][j+k] == player for k in range(chain_length)):
                return True
    
    # Check diagonals (/)
    for i in range(chain_length - 1, rows):
        for j in range(cols - chain_length + 1):
            if all(state[i-k][j+k] == player for k in range(chain_length)):
                return True
    
    return False

def game_over(state, chain_length):
    return wins(state, HUMAN, chain_length) or wins(state, COMP, chain_length)

def empty_cells(state):
    cells = []

    for x, row in enumerate(state):
        for y, cell in enumerate(row):
            if cell == 0:
                cells.append([x, y])

    return cells

def valid_move(x, y, state):
    if [x, y] in empty_cells(state):
        return True
    else:
        return False

def set_move(x, y, player, state):
    if valid_move(x, y, state):
        state[x][y] = player
        return True
    else:
        return False

def minimax(state, depth, player, alpha, beta, chain_length):
    if player == COMP:
        best = [-1, -1, -infinity]
    else:
        best = [-1, -1, +infinity]

    if depth == 0 or game_over(state, chain_length):
        score = evaluate(state, player, chain_length)
        return [-1, -1, score]

    for cell in empty_cells(state):
        x, y = cell[0], cell[1]
        state[x][y] = player
        score = minimax(state, depth - 1, -player, alpha, beta, chain_length)
        state[x][y] = 0

        if player == COMP:
            if score[2] > best[2]:
                best = [x, y, score[2]]
                alpha = max(alpha, best[2])
                if beta <= alpha:
                    break
        else:
            if score[2] < best[2]:
                best = [x, y, score[2]]
                beta = min(beta, best[2])
                if beta <= alpha:
                    break

    return best

def clean():
    os_name = platform.system().lower()
    if 'windows' in os_name:
        system('cls')
    else:
        system('clear')

def render(state, c_choice, h_choice):
    chars = {
        -1: h_choice,
        +1: c_choice,
        0: ' '
    }
    str_line = '+'.join(['-' * len(state[0])] * len(state[0]))

    print('\n' + str_line)
    for row in state:
        for cell in row:
            symbol = chars[cell]
            print(f'|{symbol}', end='')
        print('|\n' + str_line)

def ai_turn(c_choice, h_choice, state, chain_length):
    # AI's turn.
    depth = len(empty_cells(state))
    if depth == 0 or game_over(state, chain_length):
        return

    clean()
    print(f'Computer turn [{c_choice}]')
    render(state, c_choice, h_choice)

    if depth == len(state) * len(state[0]):
        moves = empty_cells(state)
        move = choice(moves)
        x, y = move[0], move[1]
    else:
        best_score = -infinity if COMP == HUMAN else +infinity
        best_move = None

        for cell in empty_cells(state):
            x, y = cell[0], cell[1]
            state[x][y] = COMP
            score = minimax(state, depth - 1, HUMAN, -infinity, +infinity, chain_length)
            state[x][y] = 0

            if (HUMAN == HUMAN and score[2] > best_score) or (HUMAN == COMP and score[2] < best_score):
                best_score = score[2]
                best_move = cell

        if best_move is not None:
            x, y = best_move[0], best_move[1]
        else:
            moves = empty_cells(state)
            move = choice(moves)
            x, y = move[0], move[1]

    set_move(x, y, COMP, state)
    time.sleep(1)

def human_turn(c_choice, h_choice, state, chain_length):
    # Human's turn.
    depth = len(empty_cells(state))
    if depth == 0 or game_over(state, chain_length):
        return

    # Dictionary of valid moves
    move = -1
    moves = {}
    count = 1

    for i in range(len(state)):
        for j in range(len(state[i])):
            moves[count] = [i, j]
            count += 1

    clean()
    print(f'Human turn [{h_choice}]')
    render(state, c_choice, h_choice)

    while move < 1 or move > len(moves):
        try:
            move = int(input(f'Use numbers (1..{len(moves)}): '))
            coord = moves[move]
            can_move = set_move(coord[0], coord[1], HUMAN, state)

            if not can_move:
                print('Bad move')
                move = -1
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

def main():
    # Main game loop.
    chain_length = int(input("Enter the chain length for winning: "))
    rows = int(input("Enter the number of rows: "))
    cols = int(input("Enter the number of columns: "))
    
    global board
    board = [[0 for _ in range(cols)] for _ in range(rows)]

    clean()
    h_choice = ''
    c_choice = ''
    first = ''

    while h_choice != 'O' and h_choice != 'X':
        try:
            h_choice = input('Choose X or O\nChosen: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    if h_choice == 'X':
        c_choice = 'O'
    else:
        c_choice = 'X'

    clean()
    while first != 'Y' and first != 'N':
        try:
            first = input('First to start?[y/n]: ').upper()
        except (EOFError, KeyboardInterrupt):
            print('Bye')
            exit()
        except (KeyError, ValueError):
            print('Bad choice')

    while len(empty_cells(board)) > 0 and not game_over(board, chain_length):
        if first == 'N':
            ai_turn(c_choice, h_choice, board, chain_length)
            first = ''

        human_turn(c_choice, h_choice, board, chain_length)
        ai_turn(c_choice, h_choice, board, chain_length)

    if wins(board, HUMAN, chain_length):
        clean()
        print(f'Human turn [{h_choice}]')
        render(board, c_choice, h_choice)
        print('YOU WIN!')
    elif wins(board, COMP, chain_length):
        clean()
        print(f'Computer turn [{c_choice}]')
        render(board, c_choice, h_choice)
        print('YOU LOSE!')
    else:
        clean()
        render(board, c_choice, h_choice)
        print('DRAW!')

if __name__ == '__main__':
    main()