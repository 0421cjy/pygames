import sys, pygame
import random

pygame.init()
screen = pygame.display.set_mode((500, 400))
pygame.display.set_caption('snake')

while 1:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                pygame.quit()
                sys.exit()

    pygame.display.update()