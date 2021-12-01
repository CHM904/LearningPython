import pygame
from pygame.constants import QUIT, SCRAP_SELECTION
pygame.init()

WindowSize = [400, 300]
screen = pygame.display.set_mode(WindowSize)
pygame.display.set_caption("Circles")
colour = pygame.color.Color('#FFFFFF')

done = False
circle_center = 200

while not done:

    if circle_center >150:
        circle_center = circle_center - 10

    pygame.draw.circle(screen, colour, [circle_center, circle_center], 50)
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

pygame.quit()

