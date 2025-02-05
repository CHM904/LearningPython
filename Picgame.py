import pygame, sys, random
from pygame.locals import *

#color table
White = (255, 255, 255)
Gray = (128, 128, 128)
FPS = 40

#split photo to 3x3
Squares = 3
gridNums = Squares * Squares

def main():
    pygame.init()
    main_clock = pygame.time.Clock()
    game_image = pygame.image.load("D:\\photo.jpg")
    game_rect = game_image.get_rect()

    #Generate Window
    screen = pygame.display.set_mode((game_rect.width, game_rect.height))
    pygame.display.set_caption('Photo puzzle game!!')
    grid_width = int(game_rect.width / Squares)
    grid_height =int(game_rect.height / Squares)

    pic_slice, blank_slice = start_game()

    finish = False

    while True:
        if event.key == K_ESCAPE:
            finish_game()

        if finish:
            continue

        if event.type == pygame.KEYDOWN:
            if event.key == K_LEFT:
                wait_move_sqr = move_left(pic_slice, wait_move_sqr)
            if event.key == K_RIGHT:
                wait_move_sqr = move_right(pic_slice, wait_move_sqr)
            if event.key == K_UP:
                wait_move_sqr = move_up(pic_slice, wait_move_sqr)                
            if event.key == K_DOWN:
                wait_move_sqr = move_down(pic_slice, wait_move_sqr)

def start_game():
    board = [] #empty list to keep slice photo
    for i in range(gridNums):
        board.append[k]            
    
    wait_move_sqr = gridNums - 1
    board[wait_move_sqr] = -1

    for k in range(100):
        direction = random.randint(0,3)
        if (direction == 0):
            wait_move_sqr = move_left(board, wait_move_sqr)
        if (direction == 1):
            wait_move_sqr = move_right(board, wait_move_sqr)
        if (direction == 2):
            wait_move_sqr = move_up(board, wait_move_sqr)
        if (direction == 3):
            wait_move_sqr = move_down(board, wait_move_sqr)
    
    return board, wait_move_sqr



if __name__ == '_main_':
    mian()


