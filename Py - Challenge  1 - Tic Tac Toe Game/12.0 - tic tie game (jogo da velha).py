# what we need to build ?
# first a board
# display this board
# play game
# handle turn
# check win
#   check rows
#   check columns
#   check diagonals
# check tie (empate)
# flip player

# creating the board 3x3
board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

# create display board


def display_board():    # imprimir a tabela na tela
    print(board[0] + " | " + board[1] + " | " + board[2])
    print(board[3] + " | " + board[4] + " | " + board[5])
    print(board[6] + " | " + board[7] + " | " + board[8])


def handle_turn(player):    # vai a vez de quem joga e mandar escolher uma posicao
    print(player + ' turn')     # player da vez
    position = int(input('Choose a position from 1-9: ')) - 1  # posicao de 1 a 9
    while True:
        while position not in [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]:  # se a posicao nao tiver entre 1 e 9
            position = int(input('Position invalid! .Choose a position from 1-9: ')) - 1    # esolher dnv

        if board[position] == '-':  # se nao tiver nenhuma jogada na posicao escolhida entao pode sair do loop
            break
        else:       # se tiver jogada na posicao entao esolher outra
            position = int(input('Hey! you cant go in there .Choose a position from 1-9: ')) - 1

    board[position] = current_player    # na posicao esolhida marcar o jogador da vez
    display_board()  # imprimir a tabela


game_still_going = True     # para verificar se alguem ganhou ou empatou
winner = None               # sem vencedor no momento caso ngm ganhe entao empatou
current_player = 'X'        # primeiro a jogar


def play_game():        # iniciar o jogo
    # display initial board
    display_board()     # mostrar a tabela

    while game_still_going:     # enquanto game still goind = true é pq ngm ganhou ou tem espaco para jogar ainda

        handle_turn(current_player)     # jogagor da vez jogar em alguma posicao
        check_if_game_over()        # depois que jogar verificar se alguem ganhou ou ainda tem espaço
        flip_player()               # se ngm ganhou entao mudar de jogador

    if winner == 'X' or winner == 'O':      # se alguem ganhou entao imprimir quem
        print(winner + ' WON.')
    elif winner == None:                    # se nao tem vencedor entao empatou
        print('Tie')


def check_if_game_over():       # verificar se ainda tem jogadas ou vencedor
    check_if_win()
    check_if_tie()


def check_if_win():
    global winner  # para ser a mesma variavel da de fora   # pra o winner ser uma variavel global

    row_winner = check_rows()  # check rows
    column_winner = check_columns()  # check columns
    diagonal_winner = check_diagonal()  # check diagonals

    if row_winner:      #
        winner = row_winner  # there war a winner
    elif column_winner:
        winner = column_winner  # there war a winner
    elif diagonal_winner:
        winner = diagonal_winner  # there war a winner
    else:
        winner = None   # there was no winner
    return


def check_rows():
    global game_still_going

    row_1 = board[0] == board[1] == board[2] != "-"  # verificar se todas essas linhas sao iguais
    row_2 = board[3] == board[4] == board[5] != "-"
    row_3 = board[6] == board[7] == board[8] != "-"

    if row_1 or row_2 or row_3:     # se uma delas forem true entao parar o jogor
        game_still_going = False
    if row_1:               # e retornar o vencedor da linha
        return board[0]
    if row_2:
        return board[3]
    if row_3:
        return board[6]


def check_columns():
    global game_still_going

    column_1 = board[0] == board[3] == board[6] != "-"  # verificar se uma das colunas sao iguais, retorna true
    column_2 = board[1] == board[4] == board[7] != "-"
    column_3 = board[2] == board[5] == board[8] != "-"

    if column_1 or column_2 or column_3:  # se for parar o jogo
        game_still_going = False
    if column_1:
        return board[0]
    if column_2:
        return board[1]
    if column_3:
        return board[2]


def check_diagonal():
    global game_still_going
    diagonal_1 = board[0] == board[4] == board[8] != "-"
    diagonal_2 = board[2] == board[4] == board[6] != "-"

    if diagonal_1 or diagonal_2:
        game_still_going = False
    if diagonal_1:
        return board[0]
    if diagonal_2:
        return board[2]


def check_if_tie():
    global game_still_going

    if "-" not in board:
        game_still_going = False
    return


def flip_player():
    global current_player

    if current_player == "X":
        current_player = "O"
    elif current_player == "O":
        current_player = "X"

    return

play_game()