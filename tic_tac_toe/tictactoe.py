

def print_board(board):
    for row in board:
        print(' | '.join(row))
        print('-'*10)

def get_player_move():
    while True:
        move = input('Enter your move (row and column 1-3): ').split()
        if len(move) ==2 and all([m.isdigit() for m in move]):
            row, col = map(int, move)
            if row in range(1,4) and col in range(1,4):
                return row-1, col-1
        print('Invalid move. Please try again.')


def check_winner(board, player):
    for row in board:
        if all([cell == player for cell in row]):
            return True

    for col in range(3):
        if all([board[row][col] == player for row in range(3)]):
            return True

    if all([board[i][i] == player for i in range(3)]) or all([board[i][2-i] == player for i in range(3)]):
        return True
    return False

def check_draw(board):
    return all([cell != ' ' for row in board for cell in row])


def main():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    current_player = 'X'

    while True:
        print_board(board)
        print(f'Player {current_player} turn')
        row, col = get_player_move()

        if board[row][col] == ' ':
            board[row][col] = current_player
        else:
            print('Cell already occupied. Try a different one.')
            continue

        if check_winner(board, current_player):
            print_board(board)
            print(f'Player {current_player} wins!')
            break

        if check_draw(board):
            print_board(board)
            break

        current_player = 'O' if current_player == 'X' else 'X'

if __name__ == '__main__':
    main()