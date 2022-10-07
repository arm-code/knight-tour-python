"""
IMPLEMENTING A CHESS BOARD USING PYGAME.
"""
from typing import Counter
import pygame
import sys
import numpy as np
import time

pygame.font.init()

BLACK = (0,0,0)
WHITE = (255,255,255)
SIZE_BOARD = 8

ROWS = np.array([2, 1, -1, -2, -2, -1, 1, 2])
COLUMNS = np.array([1, 2, 2, 1, -1, -2, -2, -1])

SIZE_SCREEN = [400,400]
WINDOW = pygame.display.set_mode(SIZE_SCREEN)

WIDTH = int(SIZE_SCREEN[0] / SIZE_BOARD)
HEIGHT = int(SIZE_SCREEN[1] / SIZE_BOARD)

TEXT = pygame.font.SysFont('comicsans', 25)

pygame.display.set_caption("CHESS BOARD")

"""
THIS FUNCTION CHECK THE VALID MOVES IN THE CHESS BOARD.
"""
def is_valid_move(visited, new_row, new_col):
    if (new_row >= 0) and (new_row < 8) and (new_col >= 0) and (new_col < 8) and (visited[new_row, new_col] == 0):
        return True
    return False

"""
THIS IS THE KNIGHT TOUR IMPLEMENTATION.
"""
def find_knight_tour(visited, row, col, move_counter):
    if move_counter == 64:
        return True
    else:
        for k in range(SIZE_BOARD):
            new_row = row + ROWS[k]
            new_col = col + COLUMNS[k]
            if is_valid_move(visited, new_row, new_col):
                move_counter = move_counter + 1
                visited[new_row, new_col] = move_counter
                if find_knight_tour(visited, new_row, new_col, move_counter):                                       
                    return True                    
                move_counter = move_counter - 1
                visited[new_row, new_col] = 0
    return False

def search(board):
    for i in range(len(board[0])):
       for j in range(len(board)):
            #if board[i,j] == key:
            draw_position(j+1, i+1, int(board[i,j]))


def draw_chess_board():
    color = 0
    for i in range (0, SIZE_SCREEN[0], WIDTH):
        for j in range(0, SIZE_SCREEN[1], HEIGHT):
            if color % 2  == 0:
                pygame.draw.rect(WINDOW, BLACK, [i, j, WIDTH, HEIGHT], 0)
            else:
                pygame.draw.rect(WINDOW, WHITE, [i, j, WIDTH, HEIGHT], 0)
            color += 1
        color += 1

def draw_position(x,y,n):    
    pos_x = (x * WIDTH) - WIDTH/2
    pos_y = (y * HEIGHT) - HEIGHT/2
    position_number = TEXT.render(str(n), True, (255,0,0))  
    WINDOW.blit(position_number, (pos_x-15, pos_y-20))
    

def main(game_state):    
    draw_chess_board()    
    pause = False 
    run = True
    while run:        
        for eventGame in pygame.event.get():
            if eventGame.type  == pygame.QUIT:
                run = False                

            if eventGame.type == pygame.KEYDOWN:                
                pause = not pause          
        
        #draw_chess_board()
        search(game_state)
         
        # REFRESH THE SCREEN 
        pygame.display.update() 

    pygame.quit()
        

if __name__ == '__main__':
    game_state =  np.zeros((SIZE_BOARD,SIZE_BOARD))
    print(game_state)
    game_state[7,0] = 1
    find_knight_tour(game_state,7,0,1) 
    print(game_state)
    main(game_state)

  
        




