import pygame
import sys
from const import load_image, height, width

pygame.init()


def start_screen(screen):  # рисует меню
    fon = pygame.transform.scale(load_image('menu.jpg'), (width, height))
    screen.blit(fon, (0, 0))
    game = 1
    while game:
        pygame.display.flip()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
    return game