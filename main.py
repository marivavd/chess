import pygame
from const import size
from menu import start_screen


def main():

    pygame.init()
    screen = pygame.display.set_mode(size)
    game = start_screen(screen) # game - 1: игра на одного человека; game - 2: игра на двух человек
    while 1:
        print(1)




while 1:
    main()