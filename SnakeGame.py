import pygame
import sys

pygame.init()
screen = pygame.display.set_mode((500,500))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()