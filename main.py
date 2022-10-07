import numpy as np
import time

rows = np.array([2, 1, -1, -2, -2, -1, 1, 2])
columns = np.array([1, 2, 2, 1, -1, -2, -2, -1])

"""
LA SIGUIENTE FUNCION RELLENA EL TABLERO DE CEROS, Y LO DEV
"""
def chess_board():
    board = np.zeros((8, 8))
    return board


def find_knight_tour(visited, row, col, move):
    if move == 64:
        print(visited)
        return True
    else:
        for k in range(8):
            rows_new = row + rows[k]
            cols_new = col + columns[k]
            if if_valid_move(visited, rows_new, cols_new):
                move = move + 1
                visited[rows_new, cols_new] = move                
                if find_knight_tour(visited, rows_new, cols_new, move):
                    return True
                move = move - 1
                visited[rows_new, cols_new] = 0
    return False


def if_valid_move(visited, row_new, col_new):
    if (row_new >= 0) and (row_new < 8) and (col_new >= 0) and (col_new < 8) and (visited[row_new, col_new] == 0):
        return True
    return False


if __name__ == '__main__':
    print(chess_board())
    chess = chess_board()
    chess[0, 0] = 1
    print(chess)

    start = time.time()
    find_knight_tour(chess, 0, 0, 1)
    print(chess)
    time.sleep(1)
    fin = time.time()
    print("Tiempo que tarda en ejecutar todos los movimientos... ", fin - start)



