from os import path
import pygame
from pygame.constants import QUIT, SCRAP_SELECTION

pygame.init()

WindowSize = [600, 600]
screen = pygame.display.set_mode(WindowSize)
pygame.display.set_caption("loading image file")

screen.fill('#FFFFFF')
img = pygame.image.load("d:\Pokemon.jpg")
img.convert()

px, py = 10, 10

move_way = 'Right'
fps = 30
trace_pokemon = pygame.time.Clock()
done = False

while not done:
    #pygame.display.flip()
    screen.fill('#FFFFFF')
    
    #if move_way == 'Right':
    #    px += 10
    #    if px == 380:
    #        move_way = 'Down'
    #elif move_way == 'Down':
    #    py += 10
    #    if py == 380:
    #        move_way = 'Left'
    #elif move_way == 'Left':
    #    px -= 10
    #    if px == 10:
    #        move_way = 'Up'
    #elif move_way == 'Up':
    #    py -= 10
    #    if py == 10:
    #        move_way = "Right"
    

    #screen.blit(img, (px, py))
    #pygame.display.update()

    # trace_pokemon.tick(fps)

    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                px -= 10
            elif event.key == pygame.K_RIGHT:
                px += 10
            elif event.key == pygame.K_DOWN:
                py += 10
            elif event.key == pygame.K_UP:
                py -= 10

        if event.type == pygame.KEYUP:
            if px<10:
                px = 10
            if px>380:
                px = 380
            if py<10:
                py = 10
            if py>380:
                py = 380
        
        screen.blit(img, (px, py))
        pygame.display.update()

        if event.type == pygame.QUIT:
            done = True

pygame.quit()